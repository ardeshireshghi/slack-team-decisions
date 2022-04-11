import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from dotenv import load_dotenv

load_dotenv()

SLACK_CLIENT_ID = os.environ['SLACK_CLIENT_ID']
SLACK_CLIENT_SECRET = os.environ['SLACK_CLIENT_SECRET']

client = WebClient(token=os.environ['SLACK_BOT_AUTH_TOKEN'])


def search(keyword):
    try:
        response = client.search_messages(
            query=keyword, count=1000, sort="timestamp", sort_dir="desc")

        messages = response.get('messages')
        if messages:
            return {
                "results": messages.get('matches'),
                "count": messages.get('total')
            }
        else:
            return None
    except SlackApiError as e:
        if e.response["ok"] is False:
            print(f"Error searching Slack: {e.response['error']}")
            raise e


def access_token_from_code(code):
    try:
        response = client.oauth_v2_access(client_id=SLACK_CLIENT_ID,
                                          client_secret=SLACK_CLIENT_SECRET, code=code)
        return response
    except SlackApiError as e:
        if e.response["ok"] is False:
            print(
                f"Error exchanging OAuth code with access token: {e.response['error']}")
            raise e


def post_message(access_token, channel_id, message):
    try:
        response = client.chat_postMessage(
            token=access_token, channel=channel_id, text=message, mrkdwn=True)
        return response
    except SlackApiError as e:
        if e.response["ok"] is False:
            print(
                f"Error posting message with Slack: {e.response['error']}")
            raise e
