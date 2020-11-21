import tweepy
import config
from ibm_watson import PersonalityInsightsV3
import json
from os.path import join
from flask import jsonify
from rate_tweets import rate_tweets

def get_results(api, user):

    return_json = {'status':1}
    public_tweets = api.user_timeline(user)

    impression = get_impression(public_tweets)
    bad_tweets = rate_tweets(public_tweets)

    return_json['first_impression'] = impression
    return_json['unprofessional_tweets'] = bad_tweets

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
