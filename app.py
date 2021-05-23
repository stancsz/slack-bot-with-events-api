import os
import sys

from flask import Flask
from slackeventsapi import SlackEventAdapter

from client_chat_post_message import client_chat_post_message
from process import process_text

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

# Init
app = Flask(__name__)
slack_bot_token = os.environ['SLACK_BOT_TOKEN']
slack_channel = os.environ['SLACK_CHANNEL']
signing_secret = os.environ['SIGNING_SECRET']


# set routes
@app.route('/')
def hello():
    return 'Hello, World!'


slack_event_adapter = SlackEventAdapter(signing_secret, '/slack/events', app)


@slack_event_adapter.on('message')
def get_event_subscriptions(events_subscription_payload):
    event = events_subscription_payload.get('event', {})
    if event.get('channel') == slack_channel:
        print(event)
        if 'bot_id' not in event:  # only process non bot messages
            process_event(event)


def process_event(event):
    text = event.get('text')
    response = process_text(text)
    if response is not None:
        print(response)
        if event.get('thread_ts') is not None:
            ts = event.get('thread_ts')
        else:
            ts = event.get('ts')
        print(ts)
        client_chat_post_message(
            slack_token=slack_bot_token,
            channel=slack_channel,
            text=response,
            thread_ts=ts
        )
    else:
        print("no intent/subroutine triggered")


def main():
    app.run()


if __name__ == '__main__':
    app.run(debug=True)
