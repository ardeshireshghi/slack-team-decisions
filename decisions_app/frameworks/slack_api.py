import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from dotenv import load_dotenv

load_dotenv()

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
