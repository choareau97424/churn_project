from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import pandas as pd
import uvicorn  # ASGI
import pickle
import pydantic
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()




import requests
from pandas.io.json import json_normalize


# Writing Excel File:
df.to_excel('Airlines.xlsx')

with open('./SimData/save_to_excel.json') as json_file:
    data = json.load(json_file)
    
import pandas as pd


import pandas as pd

pdObj = pd.read_json('export.json', orient='index')
print(pdObj)


import pandas as pd

