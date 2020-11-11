import tweepy

#API key and API secret
consumer_key = ""
consumer_secret = ""

#access token and access token secret
key = ""
secret = ""

#from the tweepy documentation href="https://docs.tweepy.org"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

#updating status method
api = tweepy.API(auth)
#api.update_status("tweepy + oauth!") #we might change the message

FILE_NAME = "last_seen.txt"

#this method doing the reading
def read_last_seen(FILE_NAME):
	file_read = open(FILE_NAME, "r")
	last_seen_id = int(file_read.read().strip())
	file_read.close()
	return last_seen_id

#this method doing the writing
def store_last_seen(FILE_NAME, last_seen_id):
	file_write = open(FILE_NAME, "w")
	file_write.write(str(last_seen_id))
	file_write.close()
	return

#return all the mentions in the timeline
#tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode="extended")
#print(tweets.text[0])

def reply():
	for tweet in reversed(tweets):
		if "#softwareengineer" in tweet.full_text.lower():	#checking that if the tweet has the hastag of softwareengineer
			print(str(tweet.id) + " - " + tweet.full_text)
			api.update_status("@" + tweet.user.screen_name + "My message goes here", tweet.id)
			api.create_favorite(tweet.id)
			api.retweet(tweet.id)
			store_last_seen(FILE_NAME, tweet.id)

while True:
	reply()
	time.sleep(2)	#every 2 seconds will call the reply function