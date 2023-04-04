from typing import Union
from fastapi import FastAPI
import requests
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/model/{submission_id}")
def download_model(submission_id: str):
    API_URL = "https://www.ebi.ac.uk/biomodels"
    response = requests.get(API_URL+"/"+submission_id+"?format=json")
    json = response.json()
    model_name = json["name"]
    filename = 'output/models.csv'
    if os.path.exists(filename):
        append_write = 'a'
    else:
        append_write = 'w'
    with open(filename, append_write) as outfile:
        line = submission_id + "\t" + model_name
        outfile.write(f'{line}\n')
        print(line+"\n")
    return json
