import sys
# Twitter stuff
import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener

# Twitter Credentials
consumer_key='9oz22usBprCmnibQ7aBYDrUdS'
consumer_secret='NoCQoE6QE7jUFK9FB4NxThVSpzadMGVg4RdimQmmz7fLrgvRd8'
access_token='44102052-4GGXCOdPYsIFBIVQ0iU85p1m9HUwxNZMeoKwrKbPL'
access_secret='41zzGdMG0PEdy3bdfeFk1GwJFYQEbyYNBoKhO0E7nUXcH'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Listener class
class Listener(StreamListener):
    def __init__(self, output_file=sys.stdout):
        super(Listener,self).__init__()
        self.output_file = output_file
    def on_status(self, status):
        print(status.text, file=self.output_file)
    def on_error(self, status_code):
        print(status_code)
        return True # don't kill the stream

# output file
output = open('stream_output.txt','w')

# list of users
users = ['@YouGov',
        '@TSEofPB',
        '@SaCoatesSky',
        '@paulwaugh',
        '@PARLYapp',
        '@suttonnick',
        '@MattSingh_',
        '@MattChorley',
        '@bbclaurak',
        '@Ladpolitics',
        '@Kevin_Maguire',
        '@JolyonMaugham',
        '@jimwaterson',
        '@IsabelOakeshott',
        '@IanDunt',
        '@MrHarryCole',
        '@GuidoFawkes',
        '@georgeeaton',
        '@faisalislam',
        '@breeallegretti',
        '@afneil',
        '@alexwickham']


# create the listener instance
listener = Listener(output_file = output)
api = tweepy.streaming.Stream(auth, listener, timeout = 60)
api.filter(follow = users)
try:
    print('Start streaming.')
    stream.sample(languages=['en'])
except KeyboardInterrupt as e :
    print("Stopped.")
finally:
    print('Done.')
    stream.disconnect()
    output.close()
