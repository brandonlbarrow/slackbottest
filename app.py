import os
from flask import Flask, Response, request, jsonify
from slackybot import SlackyBot

APP = Flask(__name__)
SLACK_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
BOT = SlackyBot(SLACK_TOKEN)

@APP.route('/', methods=['GET'])
def index():
    print("This is the root page.")
    return Response(), 200


@APP.route('/hi', methods=['POST'])
def hi():
    print("SlackyBot says hello.")
    BOT.say_hi(
        request.form.get('channel_id'),
        'Hello!'
    )
    return Response(), 200

@APP.route('/instances', methods=['POST'])
def get_instances():
    print("Getting EC2 Instances")
    BOT.get_instances(
        request.form.get('channel_id'),
    )
    return Response(), 200

@APP.route('/listen', methods=['POST'])
def listen():
    if request.get_json().get('challenge'):
        challenge = request.get_json().get('challenge')
        return Response(challenge), 200
    if request.get_json()['event']['type'] == 'app_mention' and request.get_json()['event']['text'] == '<@UBKT752JV>':
        BOT.say_hi(
            request.get_json()['event']['channel'],
            'How can I help?',
            request.get_json()['event']['user']
        )
        print(request.get_json())
    if 'who am i' in request.get_json()['event']['text'].lower():
        BOT.say_hi(
            request.get_json()['event']['channel'],
            "You are <@{}>.".format(request.get_json()['event']['user'])
        )
        print(request.get_json())
        return Response('mention success'), 200
    return Response(), 200

if __name__ == "__main__":
    APP.run(debug=True)
