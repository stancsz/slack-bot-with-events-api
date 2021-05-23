import logging

logging.basicConfig(level=logging.DEBUG)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def client_chat_post_message(slack_token="",
                             channel="",
                             text="",
                             thread_ts=""):
    """
    ref
    https://slack.dev/python-slack-sdk/web/index.html#messaging
    :return:
    """
    # slack_token = os.environ["SLACK_BOT_TOKEN"]
    client = WebClient(token=slack_token)

    try:
        if thread_ts == "":
            response = client.chat_postMessage(
                channel=channel,
                text=text
            )
        else:
            response = client.chat_postMessage(
                channel=channel,
                thread_ts=thread_ts,
                text=text
            )
        return response
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
