import os
import json
from urllib.parse import parse_qs
from decisions_app.interface_adapters.presenters.slack_decisions_presenter import SlackDecisionMessagesPresenter
from decisions_app.frameworks.slack_api import access_token_from_code, post_message, search as search_slack
from decisions_app.frameworks.database.access_token_repo import AccessTokenRepository
from decisions_app.frameworks.ui.joined_page import get_join_app_html
from dotenv import load_dotenv

load_dotenv()


DECISION_IDENTIFIER = "[Decision Record]"

access_token_repo = AccessTokenRepository()


class DecisionCommands:
    List = 'list'
    Create = 'create'


def parse_body(raw_body):
    parsed_body = parse_qs(raw_body)

    # parse_qs puts all values in a list so we fix that
    parsed_body = {key: value[0] for key, value in parsed_body.items()}
    return parsed_body


def decision_messages_with_formatting(decisions):
    presenter = SlackDecisionMessagesPresenter(decisions)
    response_body = presenter.format()
    response = {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

    return response


def create_decision(decision_message):
    formatted_decision_message = f"{DECISION_IDENTIFIER}: {decision_message}"

    response_body = {
        "response_type": "in_channel",
        "type": "mrkdwn",
        "text": formatted_decision_message
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

    return response


def list_decisions(channel_name, user_id, team_id):
    token = access_token_repo.get_token(
        team_id=team_id, type="user", user_id=user_id)

    decisions = search_slack(
        f"in:#{channel_name} {DECISION_IDENTIFIER}", access_token=token)
    print('decisions', decisions)
    return decision_messages_with_formatting(decisions)


def send_welcome_message_to_slack(user_id, bot_access_token):
    message = f"""
    :wave: Hello <@{user_id}>! Thanks for choosing Slack's  "Team Decisions" application. We are going to help you with making and managing decisions: Here is how you use decisions:


     ```/decision I made a great decision and I like to keep it```
     ```/decision```  This will show you all the decisions made
    """

    post_message(channel_id=user_id,
                 access_token=bot_access_token, message=message)


def decision_handler(event, context):
    body = event.get('body')
    parsed_body = parse_body(raw_body=body)

    decision_message = parsed_body.get('text')

    try:
        if not decision_message:
            command = DecisionCommands.List
        else:
            command = DecisionCommands.Create

        if command == DecisionCommands.Create:
            return create_decision(decision_message)
        elif command == DecisionCommands.List:
            channel_name = parsed_body.get('channel_name')
            user_id = parsed_body.get('user_id')
            team_id = parsed_body.get('team_id')

            return list_decisions(channel_name, user_id=user_id, team_id=team_id)
        else:
            raise Exception('command not supported')
    except Exception as e:
        print("Lambda decision handler error:", e)
        return {
            "statusCode": 500,
            "body": "Error handling decision command. please see logs"
        }


def oauth_handler(event, context):
    oauth_code = event.get('queryStringParameters').get('code')
    response = access_token_from_code(oauth_code)

    bot_access_token = response.get('access_token')
    user_access_token = response.get('authed_user').get('access_token')
    team_id = response.get('team').get('id')
    user_id = response.get('authed_user').get('id')

    # Save user token and bot token on S3
    access_token_repo.save_token(
        type="user", access_token=user_access_token, user_id=user_id, team_id=team_id)
    access_token_repo.save_token(
        type="bot", access_token=bot_access_token, user_id=user_id, team_id=team_id)

    # Send welcome message to slack
    send_welcome_message_to_slack(
        user_id=user_id, bot_access_token=bot_access_token)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
        },
        "body": get_join_app_html()
    }
