import os
import json
from slackclient import SlackClient

SLACK_TOKEN = os.environ.get('SLACK_BOT_TOKEN')


class SlackyBot:

    def __init__(self, token=None):

        self.slack_client = SlackClient(token)
        authenticated = self.slack_client.api_call('auth.test')
        if 'error' in authenticated and authenticated['error'] == 'invalid_auth':
            raise Exception('Authentication failed, please check your token and try again.')

    def say_hi(self, channel_id, message, mention_name=None):
        self.slack_client.api_call(
            'chat.postMessage',
            channel=channel_id,
            text=message,
            username='slackybot',
            icon_emoji=':robot_face:'
        ) 

if __name__=="__main__":
    bot = SlackyBot(SLACK_TOKEN)
    print(bot.slack_client.api_call('auth.test'))
    print(bot.slack_client.api_call('channels.list'))
