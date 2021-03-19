from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
# from controller import Controller

from response_models import Result
from object_store import ObjectStore
import boto3

import pickle
import json, os
import logging

import numpy

COMPLETED_BUCKET = os.getenv("COMPLETED_BUCKET")
PENDING_BUCKET = os.getenv("PENDING_BUCKET")

# Initialize ObjectStore
try:
    ob = ObjectStore()
except Exception as ex:
    logging.error("Error is -", ex)


app = FastAPI()

@app.get("/")
async def homepage(request: Request):
    return("Welcome to Async Job Framework")


getResponses = {
                404: {"result": Result},
                102: {"result": Result}
            }
@app.get("/getResult/{job_id}", responses=getResponses)
async def getResult(job_id: str):
    """Get the job id and try fetching the result."""
    job_id_extension = str(job_id).strip()+".json"
    try:
        result = ob.get_object(job_id_extension,COMPLETED_BUCKET)
        # check if result is available or not in completed bucket and if not available check for the job in pending bucket
        if result is None:
            result = ob.get_object(job_id_extension,PENDING_BUCKET)
            if result is None:
                return JSONResponse(status_code=404, content={"result": "No job found with given ID."})
            return JSONResponse(status_code=102, content={"result": "Job pending or being fetched."})
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