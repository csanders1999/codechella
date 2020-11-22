#import flask
import tweepy
import config
from better_profanity import profanity
import language_tool_python

def remove_twitter_chars(tweet):
    tweet_arr = tweet.split(' ')
    for word in tweet_arr:
        if len(word) <= 0 or word[0] == '@' or word[0] == '#':
            tweet_arr.remove(word)
    return ' '.join(tweet_arr)

def unprofessional(tweet):
    '''
    function to determine whether tweet is professional or not
    returns true if tweet is unprofessional, false otherwise
    '''
    tool = language_tool_python.LanguageTool('en-US')
    if profanity.contains_profanity(tweet):
        return True, 'profanity'
    elif len(tool.check(remove_twitter_chars(tweet))) > 0:
        return True, 'grammar'
    #anything else?
    else:
        return False, 'none'

def rate_tweets(tweets):
    '''
    tweets = list of tweet objects

    analyze each tweet and determine whether it is professional or not
    return list of tweets deemed unprofessional
    '''
    unprofessional_tweets = []
    for tweet in tweets:
        out = unprofessional(tweet.full_text)
        if out[0]:
            unprofessional_tweets.append({'tweet': tweet,
                                          'reason': out[1]})
    return unprofessional_tweets

'''
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='realDonaldTrump', count=5, include_rts=False, tweet_mode='extended')
unp_tweets = rate_tweets(tweets)
print(unp_tweets)
'''
