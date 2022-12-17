import logging
import boto3
from decouple import config


class SESServiceAbout:
    def __init__(self):
        self.client = boto3.client(
            'ses',
            region_name="eu-central-1",
            aws_access_key_id=config('aws_access_key_id'),
            aws_secret_access_key=config('aws_secret_access_key'),
        )

    def send_email(self, last_object):
        email = 'ice_flame@abv.bg'
        subject = f"{last_object.name} with mail {last_object.email} ask admin from Cit-Chat"
        text = last_object.message
        # logging.info('Starting email sending')
        response = self.client.send_email(
            Source='teodor.vulev@gmail.com',
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Subject': {
                    'Data': subject,
                    'Charset': 'UTF-8',
                },
                'Body': {
                    'Text': {
                        'Data': text,
                        'Charset': 'UTF-8',
                    },
                }
            },
        )
        print(response)


# sender = SESService()
# sender.send_email('ice_flame@abv.bg')


class SESServiceAppUser:
    def __init__(self):
        self.client = boto3.client(
            'ses',
            region_name="eu-central-1",
            aws_access_key_id=config('aws_access_key_id'),
            aws_secret_access_key=config('aws_secret_access_key'),
        )

    def send_email(self, email):
        # logging.info('Starting email sending')

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
        print(response)
