from botocore.client import BaseClient
import boto3
import os
import json
from botocore.exceptions import ClientError

access_key = 'AWS_ACCESS_KEY_ID'
access_value = os.getenv(access_key)
secret_key = 'AWS_SECRET_ACCESS_KEY'
secret_value = os.getenv(secret_key)


# uses credentials from environment
def s3_connect() -> BaseClient:
    s3 = boto3.client(
    's3',
    aws_access_key_id=access_value,
    aws_secret_access_key=secret_value,

)
    return s3

s3=s3_connect()
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

bucket = 'completed-bucket'
key = '1234.json'

# Fetch an object or print error if it doesnt exist.
try :
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    jsonObject = json.loads(content.read())
    print(jsonObject)
except ClientError as ex:
    if ex.response['Error']['Code'] == 'NoSuchKey':
        print('No object found - returning empty')
    else:
        raise

region = 'us-east-2'
# location = {'LocationConstraint': region}
# s3_client = boto3.client('s3',)
s3.create_bucket(ACL='private', Bucket="pend201023")