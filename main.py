from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import os 
from dotenv import dotenv_values, load_dotenv
load_dotenv()


app = FastAPI()

url = "http://localhost:8080/"

BEARER_TOKEN = dotenv_values(".env")
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}
try: 
    if BEARER_TOKEN:
        @app.get("/prompt")
        def get_data():
            if response := requests.get(url).status_code == 200:
                countries = requests.get(url + f"/countries")
                pandemics = requests.get(url + f"/pandemics")
                infections = requests.get(url + f"/infections")
                reports = requests.get(url + f"/repors")
                response = {
                    "countries": countries.json(),
                    "pandemics": pandemics.json(),
                    "infections": infections.json(),
                    "reports": reports.json()
                }
                return response
            else:
                return HTMLResponse(status_code=404)
    else:
        print("Unauthorized access: Bearer_token is not set")
except Exception as e:
    print(f"An error occurred: {e}")