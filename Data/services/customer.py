import json
import requests
import pandas as pd
import os
import glob

url= "172.50.0.4:8002"
response = requests.request("GET", url).json()
df = pd.DataFrame(response['data.csv'])
df.to_csv('data.csv')