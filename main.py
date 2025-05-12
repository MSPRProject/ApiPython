from fastapi import FastAPI
from fastapi.responses import Response
import requests
from dotenv import dotenv_values, load_dotenv
load_dotenv()


app = FastAPI()

url = "http://localhost:8080/"

BEARER_TOKEN = dotenv_values(".env")
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}

if BEARER_TOKEN is None or BEARER_TOKEN == "":
    raise ValueError("Bearer token is not set in the .env file.")

@app.get("/prompt")
def get_data():
    countries = requests.get(url + f"/countries")
    pandemics = requests.get(url + f"/pandemics")
    infections = requests.get(url + f"/infections")
    reports = requests.get(url + f"/repors")

    if countries.status_code != 200 or \
       pandemics.status_code != 200 or \
       infections.status_code != 200 or \
       reports.status_code != 200:
        return Response(status_code=500)

    response = {
        "countries": countries.json(),
        "pandemics": pandemics.json(),
        "infections": infections.json(),
        "reports": reports.json()
    }
    return response

