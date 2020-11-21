import tweepy
import config
from ibm_watson import PersonalityInsightsV3
from watson_developer_cloud import VisualRecognitionV3
import json
from os.path import join
from flask import jsonify
import re

def get_results(api, user):

    return_json = {'status':1}

    public_tweets = api.user_timeline(user, count=500)
    return_json['total_number_of_tweets'] = len(public_tweets)

    impression = get_impression(public_tweets)
    return_json['first_impression'] = impression

    unprofessional_photos = get_photos(public_tweets)
    return_json['unprofessional_photos'] = unprofessional_photos

    return(return_json)



def get_impression(public_tweets):

    personality_insights = PersonalityInsightsV3(
        version=config.myVersion,
        iam_apikey=config.myIam_apikey,
        url=config.myUrl
    )

    personality = {
        'adventurous' : 0,
        'emotionally-intelligent' : 0,
        'imaginative' : 0,
        'intellectual' : 0,

        'cautious' : 0,
        'orderly' : 0,
        'disciplined' : 0,

        'assertive' : 0,
        'cheerful' : 0,
        'outgoing' : 0,

        'modest' : 0,
        'uncompromising' : 0,
        'sympathetic' : 0,
        'trusting' : 0,

        'worry-prone' : 0,
        'melancholic' : 0,
        'self-conscious' : 0,
        'stress-prone' : 0,
    }


    newTweets = []
    for tweet in public_tweets:
        newTweets.append(tweet.text)
    tweets= {'contentItems': newTweets}

    with open('./profile.json', 'w') as fp:
        json.dump(tweets, fp, indent=2)

    with open('./profile.json') as profile_json:
        profile = personality_insights.profile(
            profile_json.read(),
            'application/json',
            content_type='application/json',
            consumption_preferences=True,
            raw_scores=True
        ).get_result()

    personality['adventurous'] += profile['personality'][0]['children'][0]['raw_score']
    personality['emotionally-intelligent'] += profile['personality'][0]['children'][2]['raw_score']
    personality['imaginative'] += profile['personality'][0]['children'][3]['raw_score']
    personality['intellectual'] += profile['personality'][0]['children'][4]['raw_score']

    personality['cautious'] += profile['personality'][1]['children'][1]['raw_score']
    personality['orderly'] += profile['personality'][1]['children'][3]['raw_score']
    personality['disciplined'] += profile['personality'][1]['children'][4]['raw_score']

    personality['assertive'] += profile['personality'][2]['children'][1]['raw_score']
    personality['cheerful'] += profile['personality'][2]['children'][2]['raw_score']
    personality['outgoing'] += profile['personality'][2]['children'][4]['raw_score']

    personality['modest'] += profile['personality'][3]['children'][2]['raw_score']
    personality['uncompromising'] += profile['personality'][3]['children'][3]['raw_score']
    personality['sympathetic'] += profile['personality'][3]['children'][4]['raw_score']
    personality['trusting'] += profile['personality'][3]['children'][5]['raw_score']

    personality['worry-prone'] += profile['personality'][4]['children'][0]['raw_score']
    personality['melancholic'] += profile['personality'][4]['children'][0]['raw_score']
    personality['self-conscious'] += profile['personality'][4]['children'][0]['raw_score']
    personality['stress-prone'] += profile['personality'][4]['children'][0]['raw_score']
    
    personalities = sorted(personality, key=personality.get, reverse=True)[:3]

    return(personalities)

def get_photos(public_tweets):
    visual_recognition = VisualRecognitionV3(config.myVersion2, iam_apikey=config.myIam_apikey2)
    unprofessional_photos = []
    alcohol_keywords = ["beer", "wine", "shot", "beer bottle", "alcoholic beverage", "stout", "ale", "brew", "mixed drink"]
    nudity_keywords = ["underwear", "undergarment", "lingerie", "bra", "panty", "underpant"]
    other_keywords = ["drug", "drugs", "party", "illegal", "inappropriate"]
    num_of_images = 0
    for tweet in public_tweets:
        if 'media' in tweet.entities and num_of_images <10:
            for image in  tweet.entities['media']:
                print("Attempting to classify possible image...")
                num_of_images += 1
                try:
                    url = image['media_url']
                    classes_result = visual_recognition.classify(url=url).get_result() # classifies image

                    # Gets json data
                    classify_data = json.dumps(classes_result["images"][0]["classifiers"][0]["classes"], indent=2)
                    # Going through every dictionary in list of json date
                    for dict in json.loads(classify_data):
                        for key, value in dict.items():
                            if value in alcohol_keywords:
                                if(len(unprofessional_photos) == 0 or unprofessional_photos[-1]['tweet'] != tweet.text):
                                    unprofessional_photos.append({'tweet': tweet.text, 'reason': 'alcohol'})
                            if value in nudity_keywords:
                                if(len(unprofessional_photos) == 0 or unprofessional_photos[-1]['tweet'] != tweet.text):
                                    unprofessional_photos.append({'tweet': tweet.text, 'reason': 'nudity'})
                            if value in other_keywords:
                                if(len(unprofessional_photos) == 0 or unprofessional_photos[-1]['tweet'] != tweet.text):
                                    unprofessional_photos.append({'tweet': tweet.text, 'reason': value})

                except:
                    print("Error clasifying image")

    return(unprofessional_photos)