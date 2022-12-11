import boto3
from django.utils.datetime_safe import datetime
from decouple import config


class SQSService:
    def __init__(self):
        self.url = "https://sqs.eu-central-1.amazonaws.com/392240374242/sendmails.fifo"
        self.client = boto3.client(
            'sqs',
            region_name="eu-central-1",
            aws_access_key_id=config('aws_access_key_id'),
            aws_secret_access_key=config('aws_secret_access_key'),
        )

    def send_message(self, email):
        self.client.send_message(
    QueueUrl=self.url,
    MessageBody=f'Sending mail to {email}',
    DelaySeconds=0,
    MessageAttributes={
        'Email': {
            'StringValue': email,
            'DataType': 'String',
        }
    },
    MessageDeduplicationId=str(datetime.utcnow().timestamp()),
    MessageGroupId=str(datetime.utcnow().timestamp()),
        )