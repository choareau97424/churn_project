# -*- coding: utf-8 -*-


# Import required modules
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from fastapi.encoders import jsonable_encoder

# from fastapi import Depends, HTTPException
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from starlette.status import HTTP_401_UNAUTHORIZED


## Schema validation
class Features(BaseModel):
    gender: Literal['Male', 'Female']
    SeniorCitizen: Literal['Yes', 'No']
    Partner: Literal['Yes', 'No']
    Dependents: Literal['Yes', 'No']
    tenure: int
    PhoneService: Literal['Yes', 'No']
    MultipleLines: Literal['Yes', 'No', 'No phone service']
    InternetService: Literal['No', 'Fiber optic', 'DSL']
    OnlineSecurity: Literal['No internet service', 'No', 'Yes']
    OnlineBackup: Literal['No internet service', 'No', 'Yes']
    DeviceProtection: Literal['No internet service', 'No', 'Yes']
    TechSupport: Literal['No internet service', 'No', 'Yes']
    StreamingTV: Literal['No internet service', 'No', 'Yes']
    StreamingMovies: Literal['No internet service', 'No', 'Yes']
    Contract: Literal['Two year', 'Month-to-month', 'One year']
    PaperlessBilling: Literal['Yes', 'No']
    PaymentMethod: Literal['Credit card (automatic)', 'Bank transfer (automatic)', 'Mailed check', 'Electronic check']
    MonthlyCharges: float
    TotalCharges: float
    
# data = {
#   'gender': 'Male',
#   'SeniorCitizen': 'Yes',
#   'Partner': 'Yes',
#   'Dependents': 'Yes',
#   'tenure': 0,
#   'PhoneService': 'Yes',
#   'MultipleLines': 'Yes',
#   'InternetService': 'No',
#   'OnlineSecurity': 'No internet service',
#   'OnlineBackup': 'No internet service',
#   'DeviceProtection': 'No internet service',
#   'TechSupport': 'No internet service',
#   'StreamingTV': 'No internet service',
#   'StreamingMovies': 'No internet service',
#   'Contract': 'Two year',
#   'PaperlessBilling': 'Yes',
#   'PaymentMethod': 'Credit card (automatic)',
#   'MonthlyCharges': 0,
#   'TotalCharges': 0
# }

# data1 = Features(
#     gender= 'Male',
#     SeniorCitizen= 'Yes',
#   Partner= 'Yes',
#   Dependents= 'Yes',
#   tenure= 0,
#   PhoneService= 'Yes',
#   MultipleLines= 'Yes',
#   InternetService= 'No',
#   OnlineSecurity= 'No internet service',
#   OnlineBackup= 'No internet service',
#   DeviceProtection= 'No internet service',
#   TechSupport= 'No internet service',
#   StreamingTV= 'No internet service',
#   StreamingMovies= 'No internet service',
#   Contract= 'Two year',
#   PaperlessBilling= 'Yes',
#   PaymentMethod= 'Credit card (automatic)',
#   MonthlyCharges= 0,
#   TotalCharges= 0
# )

# Instantiate the HTTPBasic module for Authentication
#security = HTTPBasic()

# definition of the API address
api_address = '172.50.0.2'
# API port
api_port = '8000'

# Instantiate the FastAPI module
api = FastAPI(
    title="Churn Project",
    description="Objective : Request a model API to get churn prediction" + 
    "by Author : C. Hoareau / W. Siounandan",
    version="1.0.0"
    )

# Definition of Authorized API functions Users (login + password)
authorizedUsers = {
    "christophe": "admin",
    "william": "admin"
}

# Just check that the API works
@api.get('/', name='About WEB API Status', tags=['Public'])
def home():
    return {
        'Status OK'
    }

# Get all questions for the selected test type and sort them randomly
@api.post('/prediction', name='Get the prediction from the MODEL API', tags=['Public'])
async def get_prediction(data: Features):

    try:
        encData = jsonable_encoder(data)
        newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(
            url='http://{address}:{port}/prediction'.format(address=api_address, port=api_port), 
            json=encData,
            headers=newHeaders)
        return r.json()
    
    except IndexError:
        return {}
    
