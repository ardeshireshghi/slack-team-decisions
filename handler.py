import os
import json
from urllib.parse import parse_qs
from decisions_app.interface_adapters.presenters.slack_decisions_presenter import SlackDecisionMessagesPresenter
from decisions_app.frameworks.slack_api import search as search_slack
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


def list_decisions():
    decisions = search_slack(DECISION_IDENTIFIER)
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
            return create_decision()
        elif command == DecisionCommands.List:
            return list_decisions()
        else:
            raise Exception('command not supported')
    except Exception as e:
        print("Lambda decision handler error:", e)
        return {
            "statusCode": 500,
            "body": "Error handling decision command. please see logs"
        }
