import json

import os
import boto3
import logging
import time
from typing import List

CHARSET = "UTF-8"


class SESService:
    def __init__(self):
        self.client = boto3.client(
            "see",
            region_name="eu-central-1",
        )

    def send_email(self, subject: str, body: str, receivers: List[str]):
        if not isinstance(receivers, list):
            receivers = [receivers]

        resp = self.client.send_email(
            Source="teodor.vulev@gmail.com",
            Destination={"ToAddresses": receivers,},
            Message={
                "Subject": {"Data": subject, "Charset": CHARSET},
                "Body": {"Text": {"Data": body, "Charset": CHARSET},},
            },
        )
        print("Message sent ", resp)


def lambda_handler(event, context):
    print("Starting")
    messages = event.get("Records")
    for message in messages:
        print("First sending attempt")

        email = message["messageAttributes"]["email"]["stringValue"]
        name = message["messageAttributes"]["name"]["stringValue"]
        print(email)
        print(name)
        SESService().send_email(
            f"Welcome, {name}!",
            "Welcome to our website, and thanks for your registration.",
            email,
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
