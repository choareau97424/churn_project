# -*- coding: utf-8 -*-


# Import required modules
import random
import requests
import pandas as pd
from fastapi import FastAPI, Query
from typing import Optional, List
from pydantic import BaseModel

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED


## Schema validation
class Features(BaseModel):
    Gender: int
    Parther: int
    Dependents: int
    Tenure_Months: int
    Mutiple_lines: int
    Internet_services: int
    Online_Security: int
    Online_Backup: int
    Device_Protection: int
    Tech_support: int
    Streaming_tv: int
    Streaming_movies: int
    Contract: int
    Paperless_billing: int
    Payment_method: int
    Monthly_charges: float

# Instantiate the HTTPBasic module for Authentication
security = HTTPBasic()

# Instantiate the FastAPI module
api = FastAPI(
    title="Churn Project",
    description="Objective : Request a model API to get churn prediction" + 
    "Author : C. Hoareau / W. Siounandan",
    version="1.0.0"
    )

# Definition of Authorized API functions Users (login + password)
authorizedUsers = {
    "christophe": "admin",
    "william": "admin"
}



# Just check that the API works
@api.get('/', name='About API Status', tags=['Public'])
def home():
    return {
        'Status OK'
    }

# Get all questions for the selected test type and sort them randomly
@api.get('/prediction', name='Get the prediction from the model', tags=['Public'])
def get_prediction(data: Features):

    try:
        # Import the CSV file (database)
        r = requests.post(url, json=data)
        # Definition of the "Use" dictionary
        dictUse = {}
        uniqueUse = df_use["use"].unique()
        keys = range(1,len(uniqueUse)+1) 
        values = uniqueUse
        for i in keys:
            dictUse[i] = values[i-1]
            
        return list(dictUse.items())
    except IndexError:
        return {}
    
# Get all questions for the selected subject and sort them randomly
@api.get('/getSubjectID', name='Get all "Subject" and corresponding Identification Number', tags=['Public'])
def get_subject_id():
    try:
        # Import the CSV file (database)
        df_subject = pd.read_csv('questions.csv')
        # Definition of the "Subject" dictionary
        dictSubject = {}
        uniqueSubject = df_subject["subject"].unique()
        keys = range(1,len(uniqueSubject)+1) 
        values = uniqueSubject
        for i in keys:
            dictSubject[i] = values[i-1]
            
        return list(dictSubject.items())
    except IndexError:
        return {}
    
# Get all questions for the selected test type and one or more subject, and sort them randomly
@api.get('/getQuestionList', name='Get random list of questions according the test type and subject selected', tags=['User Credentials'])
def request_question_list(numberOfQuestions:int, useID:int, subjectID:Optional[List[int]] = Query(default=None), credentials: HTTPBasicCredentials = Depends(security)):
    
    if (credentials.username, credentials.password) not in authorizedUsers.items():
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Basic"},
        )
        
    # Import the CSV file (database)
    df_request = pd.read_csv('questions.csv')
    
    # Definition of the "Use" dictionary
    dictUse = {}
    uniqueUse = df_request["use"].unique()
    keys = range(1,len(uniqueUse)+1)
    values = uniqueUse
    for i in keys:
        dictUse[i] = values[i-1]
    size_dictUse = len(dictUse)

    # Definition of the "Subject" dictionary
    dictSubject = {}
    uniqueSubject = df_request["subject"].unique()
    keys = range(1,len(uniqueSubject)+1)
    values = uniqueSubject
    for i in keys:
        dictSubject[i] = values[i-1]
    size_dictSubject = len(dictSubject)
    
    if not ((numberOfQuestions == 5) | (numberOfQuestions == 10) | (numberOfQuestions == 20)):
        return {"Number of questions must be 5, 10 or 20."}     

    if ((useID<1) | (useID>size_dictUse)):
        return {"The useID must be comprised between 1 and the maximum of use(s) available (" + str(size_dictUse) + "). Refer to the documentation for details (or use '/getUseID')."}       
    
    try:
        result = []
        if subjectID:
            
            for i in subjectID:
                 if ((i<1) | (i>size_dictSubject)):
                     return {"The subjectID must be comprised between 1 and the maximum of subject(s) available (" + str(size_dictSubject) + "). Refer to the documentation for details (or use '/getSubjectID')."}   
            
            for i in subjectID:
                useSubject = list(df_request.loc[(df_request['use']==dictUse[useID]) & (df_request['subject']==dictSubject[i])].index)
                result.append(useSubject) 
        else:
            result = list(df_request.loc[df_request['use']==dictUse[useID]].index)
            
        result = flatten_list(result)
        random.shuffle(result)
                        
        finalList = list(df_request['question'].iloc[result])
        
        return finalList[:numberOfQuestions]
    except IndexError:
        return {}
    
@api.put('/addDataToCSV', name='Create a new recod into the CSV file', tags=['Administrator Credentials'])
def add_data_to_csv(data: Features,
                 credentials: HTTPBasicCredentials = Depends(security)):
    
    if credentials.username != "admin" or credentials.password != "admin":
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Administrator account is required",
            headers={"WWW-Authenticate": "Basic"},
        )
        
        
    new_df = pd.read_csv('questions.csv')
    
    # Definition of the "Use" dictionary
    dictUse = {}
    uniqueUse = new_df["use"].unique()
    keys = range(1,len(uniqueUse)+1)
    values = uniqueUse
    for i in keys:
        dictUse[i] = values[i-1]
    size_dictUse = len(dictUse)

    # Definition of the "Subject" dictionary
    dictSubject = {}
    uniqueSubject = new_df["subject"].unique()
    keys = range(1,len(uniqueSubject)+1)
    values = uniqueSubject
    for i in keys:
        dictSubject[i] = values[i-1]
    size_dictSubject = len(dictSubject)
        
    if ((use<1) | (use>size_dictUse)):
        return {"The use must be comprised between 1 and the maximum of use(s) available (" + str(size_dictUse) + "). Refer to the documentation for details (or use '/getUseID')."}
    
    if ((subject<1) | (subject>size_dictSubject)):
        return {"The subject must be comprised between 1 and the maximum of subject(s) available (" + str(size_dictSubject) + "). Refer to the documentation for details (or use '/getSubjectID')."}   

    correctString = str(correct).replace("[","")
    correctString = correctString.replace("]","")
    correctString = correctString.replace("'","")
    
    new_question = {
        'question': question,
        'subject': dictSubject[subject],
        'use': dictUse[use],
        'correct': correctString,
        'responseA': responseA,
        'responseB': responseB,
        'responseC': responseC,
        'responseD': responseD,
        'remark': remark,
    }
    new_df = new_df.append(new_question, ignore_index=True)
    new_df.to_csv('questions.csv', index = False)
    return new_question
