import os
import boto3
from botocore.exceptions import ClientError

DECISIONS_S3_BUCKET = os.environ["DECISIONS_S3_BUCKET"]


def create_s3_client():
    return boto3.client('s3')


class AccessTokenRepository:
    def __init__(self, s3_client=None):
        self.client = s3_client if s3_client else create_s3_client()

    def get_token(self, team_id, user_id):
        pass

    def save_token(self, access_token, user_id, team_id):
        response = self.client.put_object(
            Body=access_token,
            Bucket=DECISIONS_S3_BUCKET,
            Key=f"/{team_id}/{user_id}/token",
        )

        print(response)
