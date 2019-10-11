#credit: http://docs.tweepy.org/en/v3.5.0/getting_started.html
#tweepy: open source Python package
import tweepy
import json, requests
#creating the authentication object
#auth authenciates all tweets
def api_call():
    consumer_key = "Afu2xB37IdsuxEkaR6iBIvvqz"
    consumer_secret = "85K0wlHzqPlv9tSuJmwIite0EavlYqWXPuOAbRob9v720wkVIu"
    access_token = "846363051028889601-upVMTN13332bfIkLJE3JNBBGTuaAphQ"
    access_token_secret = "4BDgP7QYcU03WfKCVGfChtvwozLgzGDNa7WH2O6vBowIt"
    # call data
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    #Creating the API object while passing in auth information
    api = tweepy.API(auth)
    results = api.search(q="gif")
    #result_type="popular"
    # tweets = results[0]
    for tweet in results:
    #     # print(tweet.media_url)

    #     # print(f"{tweet.user.name}:{tweet.extended_entities.media}")
        data_tweets = f"{tweet.user.name}:{tweet.text}"
        return data_tweets

print(api_call())
# json_str = json.dumps(tweets._json)



#Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
# public_tweets = api.home_timeline()
# # foreach through all tweets pulled
# for tweet in public_tweets:
   # printing the text stored inside the tweet object
   # print(tweet.text)
