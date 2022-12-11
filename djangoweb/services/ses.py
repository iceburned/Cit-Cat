import logging
import boto3
from decouple import config

class SESService:
    def __init__(self):
        self.client = boto3.client(
            'ses',
            region_name="eu-central-1",
            aws_access_key_id=config('aws_access_key_id'),
            aws_secret_access_key=config('aws_secret_access_key'),
        )

    def send_email(self, email):
        logging.info('Starting email sending')
        response = self.client.send_email(
            Source='teodor.vulev@gmail.com',
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Subject': {
                    'Data': 'Welcome to Cit-Cat!!!',
                    'Charset': 'UTF-8',
                },
                'Body': {
                    'Text': {
                        'Data': 'Welcome and have fun in our website',
                        'Charset': 'UTF-8',
                    },
                }
            },
        )
