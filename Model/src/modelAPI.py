# -*- coding: utf-8 -*-

# Import required modules
import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from typing import Literal
from pydantic import BaseModel


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
    
  
# Instantiate the FastAPI module
api = FastAPI(
    title="Churn Project",
    description="Objective : Run model for prediction" + 
    "by Author : C. Hoareau / W. Siounandan",
    version="1.0.0"
    )

# Just check that the API works
@api.get('/', name='About MODEL API Status', tags=['Public'])
def home():
    return {
        'Status OK'
    }

# Get all questions for the selected test type and sort them randomly
@api.post('/prediction/', name='Get the prediction from the model', tags=['Public'])
async def get_prediction(data: Features):

    try:
        
        model_file="model2.pkl"
        with open(model_file, 'rb') as f:
            model = pickle.load(f)
        
        dictData = jsonable_encoder(data)
        for key, value in dictData.items():
            dictData[key] = [value]
            
        customer = pd.DataFrame.from_dict(dictData)
        y_pred = model.predict(customer)
        #y_pred_prob = model.predict_proba(customer)[:,1]
        
        return  y_pred[0] #str(y_pred_prob) + y_pred[0]        

    except IndexError:
        return {}
    
