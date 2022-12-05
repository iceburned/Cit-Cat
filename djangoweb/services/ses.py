import logging
import boto3


class SESService:
    def __init__(self):
        self.client = boto3.client(
            'ses',
            region_name="eu-central-1",
            aws_access_key_id='AKIAVWU2ZEHRJV62EBQN',
            aws_secret_access_key='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',
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
