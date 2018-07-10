import os
import json
from pprint import pprint
from slackclient import SlackClient
from slackybot_ec2.slackybot_ec2 import SlackyBotEC2

SLACK_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
AWS_PROFILE = os.environ.get('SLACKBOT_AWS_PROFILE')

class SlackyBot:

    def __init__(self, token=None):

        self.slack_client = SlackClient(token)
        authenticated = self.slack_client.api_call('auth.test')
        if 'error' in authenticated and authenticated['error'] == 'invalid_auth':
            raise Exception('Authentication failed, please check your token and try again.')
        
        self.ec2_client = SlackyBotEC2(AWS_PROFILE)

    def say_hi(self, channel_id, message, mention_name=None):
        self.slack_client.api_call(
            'chat.postMessage',
            channel=channel_id,
            text=message,
            username='slackybot',
            icon_emoji=':robot_face:'
        )
    
    def get_instances(self, channel_id, mention_name=None):
        instances = []
        for i in self.ec2_client.get_running_instances()['Reservations']:
            for x in i['Instances']:
                instances.append(
                    {
                        x['InstanceId']:[
                            {
                                x['Tags'][0]['Key']: x['Tags'][0]['Value']
                            }, {
                                'ip': x['PublicIpAddress']
                            }, {
                                'instanceType': x['InstanceType']
                            }
                        ]}
                )

        self.slack_client.api_call(
            'chat.postMessage',
            channel=channel_id,
            text=str(instances),
            username='slackybot',
            icon_emoji=':robot_face:'
        )


if __name__=="__main__":
    bot = SlackyBot(SLACK_TOKEN)
    print(bot.slack_client.api_call('auth.test'))
    print(bot.slack_client.api_call('channels.list'))
