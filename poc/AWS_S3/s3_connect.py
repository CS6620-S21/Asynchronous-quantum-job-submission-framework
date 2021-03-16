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
s3.create_bucket(ACL='private', Bucket="pend201023")


# Upload a json object to S3
json_string = '{"qobj_id": "e533279d-3cd7-4bcd-a5a8-962f3547f899", "header": {}, "config": {"shots": 1024, "memory": false, "parameter_binds": [], "init_qubits": true, "memory_slots": 2, "n_qubits": 2}, "schema_version": "1.3.0", "type": "QASM", "experiments": [{"config": {"n_qubits": 2, "memory_slots": 2}, "header": {"qubit_labels": [["q", 0], ["q", 1]], "n_qubits": 2, "qreg_sizes": [["q", 2]], "clbit_labels": [["c", 0], ["c", 1]], "memory_slots": 2, "creg_sizes": [["c", 2]], "name": "circuit7", "global_phase": 0.0}, "instructions": [{"name": "u2", "params": [0.0, 3.141592653589793], "qubits": [0]}, {"name": "cx", "qubits": [0, 1]}, {"name": "measure", "qubits": [0], "memory": [0]}, {"name": "measure", "qubits": [1], "memory": [1]}]}]}'
json_body = json.loads(json_string)

s3.put_object(
     Body=str(json.dumps(json_body)),
     Bucket=bucket,
     Key='4568.json'
)


# Delete object
s3.delete_object(Bucket=bucket, Key='4568.json')