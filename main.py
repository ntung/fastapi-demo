from typing import Union
from fastapi import FastAPI
import requests
import os

from subprocess import Popen, PIPE

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/model/list")
def list_biomodels():
    # https://stackoverflow.com/a/10501355/865603
    import uuid
    filename = str(uuid.uuid4())

    # https://www.bswen.com/2018/04/python-How-to-generate-random-large-file-using-python.html
    import random
    import string


@app.get("/testssh")
def test_ssh():
    stdout, stderr = Popen(['ssh', 'codondc', 'cd /homes/tc_pst03/testbsub; sh task1.sh'], stdout=PIPE).communicate()
    return { "output": stdout }


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
