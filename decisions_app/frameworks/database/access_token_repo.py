import os
import boto3
import json
from botocore.exceptions import ClientError

DECISIONS_S3_BUCKET = os.environ["DECISIONS_S3_BUCKET"]


def create_s3_client():
    return boto3.client('s3')


class AccessTokenRepository:
    def __init__(self, s3_client=None):
        self.client = s3_client if s3_client else create_s3_client()

    def get_token(self, type, team_id, user_id=None):
        storage_key = self._get_storage_key(
            type=type, team_id=team_id, user_id=user_id)
        response = self.client.get_object(
            Bucket=DECISIONS_S3_BUCKET,
            Key=storage_key,
        )
        parsed_response = response.get('Body').read().decode("utf-8")
        return parsed_response

    def save_token(self, type, access_token, team_id, user_id=None):
        storage_key = self._get_storage_key(
            type=type, team_id=team_id, user_id=user_id)
        response = self.client.put_object(
            Body=access_token,
            Bucket=DECISIONS_S3_BUCKET,
            Key=storage_key,
        )

        return response

    def _get_storage_key(self, type, team_id, user_id=None):
        if type == 'user':
            return f"/{team_id}/{user_id}/{self._token_name(type)}"
        else:
            return f"/{team_id}/{self._token_name(type)}"

    def _token_name(self, type):
        return 'user_token' if type == 'user' else 'bot_token'
