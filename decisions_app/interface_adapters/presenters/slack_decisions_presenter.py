from datetime import datetime


def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%b-%d %H:%M:%S')


class SlackDecisionMessagesPresenter:
    def __init__(self, decisions):
        self.decision_results = decisions['results']
        self.message_count = decisions['count']

    def format(self):
        formatted = {
            "blocks": [{
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"Total team Decisions: {self.message_count}",
                    "emoji": True
                }
            }]
        }

        for decision in self.decision_results:
            decision_blocks = [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": f"Created at: {format_time(float(decision['ts']))}",
                        "emoji": True
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Message details*"
                    },
                    "fields": [{
                        "type": "mrkdwn",
                        "text": decision['text']
                    },
                        {
                        "type": "mrkdwn",
                        "text": decision['permalink']
                    }]
                }
            ]
            formatted['blocks'].extend(decision_blocks)

        return formatted
