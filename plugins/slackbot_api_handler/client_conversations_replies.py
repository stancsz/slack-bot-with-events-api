import logging
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def client_conversations_replies(slack_token="",
                                 channel="",
                                 retrieve_messages_ts=0
                                 ):
    # WebClient insantiates a client that can call API methods
    # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
    client = WebClient(token=slack_token)
    # ID of channel that the message exists in
    conversation_id = channel

    try:
        # Call the conversations.history method using the WebClient
        # The client passes the token you included in initialization
        result = client.conversations_replies(
            channel=conversation_id,
            inclusive=True,
            ts=retrieve_messages_ts
        )
        # Print message text
        # print(result)
        return result

    except SlackApiError as e:
        logging.error("Error creating conversation: {}".format(e))
        pass
