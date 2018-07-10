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

if __name__ == "__main__":
    APP.run(debug=True)
