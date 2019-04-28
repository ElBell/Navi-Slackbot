import os
import time

from websocket import WebSocketConnectionClosedException

from event import Event
from slackclient import SlackClient


class Bot(object):
    def __init__(self):
        self.slack_client = SlackClient(os.environ["BOT_SLACK_API_TOKEN"])
        self.bot_name = "navi"
        self.bot_id = self.get_bot_id()
        if self.bot_id is None:
            exit("Error, could not find " + self.bot_name)
        self.event = Event(self)
        self.listen()

    def get_bot_id(self):
        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == self.bot_name:
                    return "<@" + user.get('id') + ">"
            return None

    def listen(self):
        if self.slack_client.rtm_connect():
            print("Successfully connected, listening for events")
            while True:
                try:
                    self.event.wait_for_event()
                    time.sleep(1)
                except WebSocketConnectionClosedException:
                    self.slack_client.rtm_connect()
        else:
            print(self.slack_client.api_call('rtm.connect'))
