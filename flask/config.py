import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Twitter
consumer_key = 'A7RMojUNL3VoKIsfwMXwAa7kg'
consumer_secret = '8arpUvO5Qbx1wqIZzkCFZLzmuAh0nvJ5vJEZA6oqQVm6fOenAn'
access_token = '2172576189-VvP3GI9HMcqBosepZnp102dt4BjIvE6cPHsa5k4'
access_token_secret =  'hzPUseQRRGkRA14SVUEX954Ez4hUFLDdLRgvMSFVvKX6L'

BEARER = 'AAAAAAAAAAAAAAAAAAAAAFXCJwEAAAAAmkg1dTXfXce%2F897r6y3rw3FDF90%3DdpRdQKLbv1ZcaducGDmB8jSUoHqKGSxwEEsIkGZhE9k3LkDDeC'

# IBM 
myVersion = '2017-10-13'
myIam_apikey = 'A8AfuUIaitSUSstz5htAvYY7XU7_n-Uvms5sAdPwsy8v'
myUrl = 'https://api.us-east.personality-insights.watson.cloud.ibm.com/instances/b7bf9a23-7b2f-430e-9b54-434f4e45451c'

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
