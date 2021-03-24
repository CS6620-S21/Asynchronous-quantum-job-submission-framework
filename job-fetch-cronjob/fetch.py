  
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

This is the job fetch cron-job that fetches all the pending jobs and checks if their result is available.
And moves the completed jobs to the Completed Bucket. 
"""

import os, logging
from qiskit import IBMQ
from api.object_store import ObjectStore

COMPLETED_BUCKET = os.getenv("COMPLETED_BUCKET")
PENDING_BUCKET = os.getenv("PENDING_BUCKET")
BACKEND = os.getenv("BACKEND")

# Initialize ObjectStore
try:
    ob = ObjectStore()
except Exception as ex:
    logging.error("Error is -", ex)


def init_backend():
    """Returns the backend to work with in the cron job"""
    token=os.getenv('BACKEND_TOKEN')
    IBMQ.save_account(token)
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q')
    IBMQ.get_provider(group='open')
    backend = provider.get_backend(BACKEND)
    return backend

def run_fetch_job():
    backend = init_backend()
    # Run for all pending objects 
    for pending_key in ob.get_all_objects(PENDING_BUCKET):
        # Process the pending object
        try:
            job_returned = backend.retrieve_job("605b99ca8057906f0a9dc2de")
        except Exception as ex:
            






if __name__ == "__main__":
    run_fetch_job()