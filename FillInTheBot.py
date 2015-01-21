__author__ = 'victoriabetts'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import configparser
import json
import blankfiller

bfill = blankfiller.BlankFiller()

config = configparser.ConfigParser()
config.read('.twitter')

consumer_key = config.get('apikey', 'key')
consumer_secret = config.get('apikey', 'secret')
access_token = config.get('token', 'token')
access_token_secret = config.get('token', 'secret')
stream_rule = config.get('app', 'rule')
account_screen_name = config.get('app', 'account_screen_name').lower() 
account_user_id = config.get('app', 'account_user_id')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterApi = API(auth)

class ReplyToTweet(StreamListener):
    
    def stripPrefix(self, sentence, prefix):
        if sentence.lower().startswith(prefix.lower()):
            return sentence[len(prefix):]
        else:
            return sentence
    
    def make_reply(self, tweet, user):
        template = self.stripPrefix(tweet, '@' + account_screen_name + ' ')
        replyText = '.@' + user + ' ' + bfill.fill_in_the_blanks(template)
        #check if repsonse is over 140 char
        if len(replyText) > 140:
            replyText = replyText[0:137] + '...'
        return replyText

    def on_data(self, data):
        print (data)
        tweet = json.loads(data.strip())
        
        retweeted = tweet.get('retweeted')
        from_self = tweet.get('user',{}).get('id_str','') == account_user_id

        if retweeted is not None and not retweeted and not from_self:

            tweetId = tweet.get('id_str')
            screenName = tweet.get('user',{}).get('screen_name')
            tweetText = tweet.get('text')
            replyText = self.make_reply(tweetText, screenName)
            if replyText == '':
                return
            print('Tweet ID: ' + tweetId)
            print('From: ' + screenName)
            print('Tweet Text: ' + tweetText)
            print('Reply Text: ' + replyText)

            # If rate limited, the status posts should be queued up and sent on an interval
            twitterApi.update_status(replyText, tweetId)

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    streamListener = ReplyToTweet()
    twitterStream = Stream(auth, streamListener)
    twitterStream.userstream(_with='user')



