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
        return False # don't kill the stream

# output file
output = open('stream_output.txt','w')

# list of users
users = ['14810076',# @YouGov
        '1117418828', # @TSEofPB
        # '@SaCoatesSky', this one not working
        '26985345',# @paulwaugh
        '2861345003',# @PARLYapp
        '21910500', # @suttonnick
        '37072353', # @MattSingh_
        '66673916', # @MattChorley
        '61183568', # @bbclaurak
        '40015623', # @Ladpolitics
        '60886384', # @Kevin_Maguire
        '406842374', # @JolyonMaugham
        '25275453', # @jimwaterson
        '437814330', # @IsabelOakeshott
        '21202851', # @IanDunt
        '15348883', # @MrHarryCole
        '465973', # @GuidoFawkes
        '20668369', # @georgeeaton
        '22812734', # @faisalislam
        '92127426', # @breeallegretti
        '136004952', # @afneil
        '405769757', #@alexwickham
        ]


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
