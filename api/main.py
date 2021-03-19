from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
# from controller import Controller
from starlette.responses import PlainTextResponse

from object_store import ObjectStore
import boto3

import pickle
import json, os
import logging

import numpy

COMPLETED_BUCKET = os.getenv("COMPLETED_BUCKET")
PENDING_BUCKET = os.getenv("PENDING_BUCKET")
s3 = boto3.client("s3")
# Initialize ObjectStore
try:
    ob = ObjectStore()
except Exception as ex:
    logging.error("Error is -", ex)


app = FastAPI()

@app.get("/")
async def homepage(request: Request):
    return("Welcome to Async Job Framework")


@app.get("/getResult/{job_id}")
async def getResult(job_id: str):
    """Get the job id and try fetching the result."""
    # TODO add error response for user, add logic to check in pending bucket if not found in completed.
    job_id_extension = str(job_id).strip()+".json"
    try:
        result = ob.get_object(job_id_extension,COMPLETED_BUCKET)
        #check if result is available or not in completed bucket and if not available check for the job in pending bucket
        if result is None:
            for key in s3.list_objects(Bucket='quantumpending')['Contents']:
                res= (key['Key'])
                if(res==job_id_extension):
                    return PlainTextResponse(str("No results found,Job still pending"), status_code=201)

                else:
                    return PlainTextResponse(str("Given job Id doesn't exist"), status_code=404)

        else:
            return result
    except Exception as ex:
        logging.error("Error is -", ex)


@app.post("/submit/")
async def submit(request: Request):
    print("request: ", request)
    # body = await request.json()
    # print("--------------------------------------------------------------")
    # print("Body: \n", body)
    # print("Type of body", type(body))
    # ctl = Controller()
    # # ctl.submit(body)

    # return ctl.submit(body)