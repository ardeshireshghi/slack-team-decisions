import os
import json
from urllib.parse import parse_qs
from decisions_app.interface_adapters.presenters.slack_decisions_presenter import SlackDecisionMessagesPresenter
from decisions_app.frameworks.slack_api import access_token_from_code, search as search_slack
from dotenv import load_dotenv

load_dotenv()


SLACK_REQUEST_VERIFY_TOKEN = os.environ["SLACK_TOKEN"]
DECISION_IDENTIFIER = "[Decision Record]"


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


def list_decisions(channel_name):
    decisions = search_slack(f"in:#{channel_name} {DECISION_IDENTIFIER}")
    return decision_messages_with_formatting(decisions)


def decision_handler(event, context):
    body = event.get('body')
    parsed_body = parse_body(raw_body=body)
    slack_token = parsed_body.get('token')

    # Validate slack token
    if slack_token != SLACK_REQUEST_VERIFY_TOKEN:
        return {
            "statusCode": 401,
            "body": "Not Authorized"
        }

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

            return list_decisions(channel_name)
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

    # TODO: Store team-id (response.team.id)/user-id(response.authed_user.id)/token in S3
    # We then need to read the value from S3 on the decision_handler calls and pass it to
    # search_slack call
    return {
        "statusCode": 200,
        "body": json.dumps({
            "accessToken": response.get('authed_user').get('access_token')
        })
    }
