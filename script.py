


# from twython import Twython
#import requests


#APP_KEY = 'YtfSE01GYJEax2rZvwS1qyCoh'
#APP_SECRET = 'KJqh30QursEPyfR9PEXwkYbHHO3pdcnBFALaldolyTqZPe9d0c'

#twitter = Twython(APP_KEY, APP_SECRET)

#auth = twitter.get_authentication_tokens(callback_url='https://google.com')

#print auth

#OAUTH_TOKEN = auth['oauth_token']
#OAUTH_TOKEN_SECRET = auth['secret_oauth_token']

#response = requests.get(auth['auth_url'])

#print response.content

#twitter = Twython(APP_KEY, APP_SECRET,
#                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#final_step = twitter.get_authorized_tokens()





from twython import Twython
import time

import reddit

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

counter = 0


while True:
    message = reddit.getRandomComment()
    twitter.update_status(status=message)
    print("Tweeted: {}".format(message))
    #counter +=1
    time.sleep(60*15)








