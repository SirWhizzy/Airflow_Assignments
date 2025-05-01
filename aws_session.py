import os

import boto3

from dotenv import load_dotenv

load_dotenv()


def aws_session():
    session = boto3.Session(
    aws_access_key_id=os.getenv('aws_access_key'),
    aws_secret_access_key=os.getenv('aws_secret_key'),
    region_name=os.getenv('region'))
    return session
