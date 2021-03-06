  
#!/usr/bin/env python3
# Async Job
# Copyright(C) 2021 Team Async 
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Object Store Helper Library.

This library contains all the methods we would be using to interact with the object store 
and other helper methods we need for file operations. 
"""

from copy import Error
from typing import List
from botocore.exceptions import ClientError
import boto3
import os
import json
import logging


COMPLETED_BUCKET = os.getenv("COMPLETED_BUCKET")
PENDING_BUCKET = os.getenv("PENDING_BUCKET")
BUCKETS = [COMPLETED_BUCKET, PENDING_BUCKET]

class ObjectStore:
    
    def __init__(self) -> None:
        """
        Checks for AWS Credentials in environment and instantiate objectstore class.
        Create the Pending (containing the Retry Bucket) and Completed Bucket if they don't exist. 
        """
        access_value = os.getenv("AWS_ACCESS_KEY_ID")
        secret_value = os.getenv("AWS_SECRET_ACCESS_KEY")
        try:
            self.s3 = boto3.client('s3', aws_access_key_id=access_value, aws_secret_access_key=secret_value)
        except Error as err:
            logging.error("Failed to create client")
            raise
        
        _existing_Buckets = [o["Name"] for o in self.s3.list_buckets().get("Buckets")]
        logging.info(_existing_Buckets)
        # Check if pending and complete buckets exist.
        for bucket in BUCKETS:
            if bucket not in _existing_Buckets:
                logging.info(f"{bucket} doesn't exist, so creating.")
                response = self.s3.create_bucket(
                                ACL = "private",
                                Bucket=bucket,
                            )
    
    def put_object(self, job_body: dict, file_name: str, bucket_name: str) -> bool:
        """
        Takes an json and a file name and puts the object in the s3 bucket 
        """ 
        try:
            self.s3.put_object(
                Body=str(json.dumps(job_body)),
                Bucket=bucket_name,
                Key=file_name
            )
            return True
        except ClientError as ex:
            logging.error("Object couldn't be inserted", ex)
            return False
        except Exception as ex:
            logging.error("Object couldn't be inserted", ex)
            return False

    def delete_object(self, key: str, bucket_name: str) -> bool:
        """
        Takes in a name of a file and removes the file from the specified bucket.
        Returns a boolean which is true if the operation is successfully. false if it fails.
        :param bucket_name: The bucket from which to delete the file.
        :param key: The name of the file to be removed from the pending bucket.
        :return: true if the remove operation is successful, false if it isn't.
        """
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=key)
            return True
        except ClientError as ex:
            logging.error("Removing file failed", ex)
            return False

    def get_object(self, key: str, bucket_name: str) -> json:
        """
        This method takes in the name(job id) of the job object as key, fetches it from the the passed bucket name
        and returns it as a JSON Object.
        :param bucket_name: The name of the bucket from which to fetch the file.
        :param key: Name of the object(job id).
        :return: Json object if an object with the same name as the key is found in the bucket. None is returned
        If there is no object with the same name as the key.
        """
        try:
            response = self.s3.get_object(Bucket=bucket_name, Key=key)
            content = response['Body']
            json_object = json.loads(content.read())
            return json_object
        except ClientError as ex:
            if ex.response['Error']['Code'] == 'NoSuchKey':
                logging.error('No object found - returning empty')
                return None
            else:
                raise

    def get_all_objects(self, bucket_name: str) -> List:
        """
        Takes an bucket and returns any 1000 objects in it.
        """
        try:
            files = []
            obj_list = self.s3.list_objects_v2(Bucket=bucket_name)
            if obj_list.get('Contents'):
                for key in obj_list['Contents']:
                    files.append(key['Key'])
            return files
        except ClientError as ex:
            logging.error(ex)
