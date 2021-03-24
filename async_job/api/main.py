from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
# from controller import Controller

import pickle
import json

import numpy

app = FastAPI()

@app.get("/")
async def homepage(request: Request):
    return("Welcome to Async Job Framework")

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
