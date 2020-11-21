#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os
import tweepy
import config
from ibm_watson import PersonalityInsightsV3
import json
from os.path import join
from flask import jsonify
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

@app.route('/insights/')
def insights():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    api = tweepy.API(auth)

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


    user = request.args.get('q')
    public_tweets = api.user_timeline(user)
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
    print(sorted(personality, key=personality.get, reverse=True))
    return render_template('pages/personality-insights.html', tweets=public_tweets, personalities=personalities)

@app.route('/view/')
def view():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    api = tweepy.API(auth)

    try:
        user = request.args.get('q')
        public_tweets = api.user_timeline(user)
    except:
        return(jsonify({"Error": "Error"}))
    return(jsonify({"Success": "Sucecss"}))
    
# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
