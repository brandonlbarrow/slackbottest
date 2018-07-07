import os
from flask import Flask, Response, request

APP = Flask(__name__)
SLACK_TOKEN = os.environ.get('SLACK_BOT_TOKEN')

@APP.route('/', methods=['GET'])
def index():
    print("This is the root page.")
    return Response(), 200

@APP.route('/hi', methods=['POST'])
def hi():
    print("Hello!")
    return Response(), 200

if __name__ == "__main__":
    APP.run(debug=True)