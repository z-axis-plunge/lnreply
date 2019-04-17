#lnreply.py

from twython import TwythonStreamer
from twython import Twython
from auth import (consumer_key, consumer_secret, access_token,
                  access_token_secret)
import subprocess


class MyStreamer(TwythonStreamer, Twython):
    subprocess = __import__('subprocess')

    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']

            ln = subprocess.Popen(["lncli", "addinvoice", "21000"],
                                  stdout=subprocess.PIPE)
            pay_req_deet = ln.communicate()[0]
            pr = pay_req_deet.split()
            twitter.update_status(
                status="@{} pay deets: {}".format(username, pr[4]))


stream = MyStreamer(consumer_key, consumer_secret, access_token,
                    access_token_secret)

twitter = Twython(consumer_key, consumer_secret, access_token,
                  access_token_secret)

MyStreamer.subprocess
stream.statuses.filter(track='#stacksonscotty')
