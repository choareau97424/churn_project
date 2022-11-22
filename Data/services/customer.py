import json
import requests
import pandas as pd
import os
import csv
from fastapi import FastAPI

# creating a GET request
f = requests.get("172.50.0.4:8002")
    customer=json.loads(f.read())
    headers = customer[0].keys()
    
def transform_data_into_csv(n_files=None):
    parent_folder = '/app/raw_files'
    files = sorted(os.listdir(parent_folder), reverse=True)
    if n_files:
        files = files[:n_files]
    dfs = []
    df = pd.DataFrame(dfs)
    
    writer =csv.DictWriter(f,fieldnames=headers)
    writer.writeheader()
    for custo in customer:
        writer.writerow(custo)
