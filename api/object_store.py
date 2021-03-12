  
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

class ObjectStore:
    def __init__(self) -> None:
        """
        Checks for AWS Credentials in environment and instantiate objectstore class.
        Create the Pending (containing the Retry Bucket) and Completed Bucket if they don't exist. 
        """
        pass


    def _list_buckets() -> str:
        pass

    
    def create_job(job_body: dict, backend_id: str = None) -> str:
        """
        If backend_id is null, put in pending bucket anyway without backend id. 
        Generate metadata json also.
        Returns the job id to user (this we generate.)
        """

    def get_result()