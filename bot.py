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



if __name__=="__main__":
    bot = SlackyBot(SLACK_TOKEN)
    print(bot.slack_client.api_call('auth.test'))
    print(bot.slack_client.api_call('channels.list'))
