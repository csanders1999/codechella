#import flask
import tweepy
import config


def remove_twitter_chars(tweet):
    tweet_arr = tweet.split(' ')
    for word in tweet_arr:
        if len(word) <= 0 or word[0] == '@' or word[0] == '#':
            tweet_arr.remove(word)
    return ' '.join(tweet_arr)

def unprofessional(tweet, profane_words):
    '''
    function to determine whether tweet is professional or not
    returns true if tweet is unprofessional, false otherwise
    '''
    #tool = language_tool_python.LanguageTool('en-US')
    for word in tweet.split(" "):
        if word in profane_words:
            return True, 'profanity'
    return False, 'none'

def rate_tweets(tweets):
    '''
    tweets = list of tweet objects

    analyze each tweet and determine whether it is professional or not
    return list of tweets deemed unprofessional
    '''
    profane_words = []
    with open('flask/profanity_wordlist.txt', 'r') as f:
        for line in f:
            profane_words.append(line.strip())
    unprofessional_tweets = []
    for tweet in tweets:
        print("Analyzing tweet.....")
        out = unprofessional(tweet.full_text, profane_words)
        if out[0]:
            unprofessional_tweets.append({'tweet': tweet.full_text,
                                          'reason': out[1],
                                          'id': tweet.id})
    return unprofessional_tweets

'''
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='notviking', count=50, include_rts=False, tweet_mode='extended')
unp_tweets = rate_tweets(tweets)
for tweet in unp_tweets:
    print(tweet['tweet'])
'''
