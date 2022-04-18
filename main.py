""" 
CREATED: 2022-04-18 by Anshumali Karna <

Contact:
Instagram: @anshumalii
Twitter: @anshumaIi
Github: @anshumalivfx

Disclaimer:
This is a free script. You are free to use, modify and redistribute it. 

Inquiries: 
Please contact me at the above contact methods. or email me at anshumali.karna99@gmail.com
"""

import tweepy
from flask import Flask, render_template, request
from decouple import config
consumer_key= config('API_KEY')
consumer_secret= config('API_SECRET_KEY')
access_token= config('ACCESS_TOKEN')
access_token_secret= config('ACCESS_TOKEN_SECRET_KEY')

app = Flask(__name__)

# auth = tweepy.OAuthHandler("tloXTzvTnJL6dmTLKfPnUNwkx", "P4wLoG4SbzLB4XpyocFXuj61x5JrmB6txZGkhHN1XC9f53sJpV")
# auth.set_access_token("2183970876-OaUy2uIjNCtG16Nijd3PEDTmDsXn9kHsqFMqwE9", "3vo9lcpCYcdhwoccJGwMkgNzMjAiPup6Wn5NcuT1lPVek")
# api = tweepy.API(auth)
# tweet = "Awesome Elon buying 'Titter' is a joke"
# if(api.update_status(status=(tweet))):
#     print ("Done!")
# else:
#     print ("Failed!")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/tweet', methods=['POST', 'GET'])
def tweet():
    client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret)
    query = request.form['tweet']
    try:
        client.create_tweet(text=query)
        success = "Tweet posted successfully!"
        return render_template('index.html', success=success)
    except:
        error = True
        return render_template('index.html', error=error)
    
    
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)

