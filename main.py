from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

url = "http://localhost:8080/"
try: 
    @app.get("/countries")
    def get_countries():
        if response := requests.get(url + "countries").status_code == 200:
            response = requests.get(url + "countries")
            return response.json()
        else:
            return HTMLResponse(status_code=404)


    @app.get("/countries/{country_id}")
    def get_country(country_id: int):
        if response := requests.get(url + f"countries/{country_id}").status_code == 200:
            response = requests.get(url + f"countries/{country_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.get("/pandemics")
    def get_pandemics():
        if response := requests.get(url + "pandemics").status_code == 200:
            response = requests.get(url + "pandemics")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.get("/pandemics/{pandemic_id}")
    def get_pandemic(pandemic_id: int):
        if response := requests.get(url + f"pandemics/{pandemic_id}").status_code == 200:
            response = requests.get(url + f"pandemics/{pandemic_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.get("/infections")
    def get_infections():
        if response := requests.get(url + "infections").status_code == 200:
            response = requests.get(url + "infections")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.get("/infections/{infection_id}")
    def get_infections(infection_id: int):
        if response := requests.get(url + f"infections/{infection_id}").status_code == 200:
            response = requests.get(url + f"infections/{infection_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.get("/reports")
    def get_reports():
        if response := requests.get(url + "reports").status_code == 200:
            response = requests.get(url + "reports")
            return response.json()
        else:
            return HTMLResponse(status_code=404)
        

    @app.get("/reports/{report_id}")
    def get_report(report_id: int):
        if response := requests.get(url + f"reports/{report_id}").status_code == 200:
            response = requests.get(url + f"reports/{report_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.get("/infections/pandemics/{pandemic_id}")
    def get_infections_by_pandemic(pandemic_id: int):
        if response := requests.get(url + f"infections/pandemics/{pandemic_id}").status_code == 200:
            response = requests.get(url + f"infections/pandemics/{pandemic_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.get("/infections/countries/{country_id}")
    def get_infections_by_country(country_id: int):
        if response := requests.get(url + f"infections/countries/{country_id}").status_code == 200:
            response = requests.get(url + f"infections/countries/{country_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.get("/reports/pandemics/{pandemic_id}")
    def get_reports_by_pandemic(pandemic_id: int):
        if response := requests.get(url + f"reports/pandemics/{pandemic_id}").status_code == 200:
            response = requests.get(url + f"reports/pandemics/{pandemic_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)
        

    @app.get("/reports/countries/{country_id}")
    def get_reports_by_country(country_id: int):
        if response := requests.get(url + f"reports/countries/{country_id}").status_code == 200:
            response = requests.get(url + f"reports/countries/{country_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.get("/reports/{date}")
    def get_reports_by_date(date: str):
        if response := requests.get(url + f"reports/{date}").status_code == 200:
            response = requests.get(url + f"reports/{date}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.post("/countries")
    def create_country(country: dict):
        if response := requests.post(url + "countries").status_code == 200:
            response = requests.post(url + "countries", json=country)
            return response.json()
        else:
            return HTMLResponse(status_code=404)
        

    @app.post("/pandemics")
    def create_pandemic(pandemic: dict):
        if response := requests.post(url + "pandemics").status_code == 200:
            response = requests.post(url + "pandemics", json=pandemic)
            return response.json()
        else:
            return HTMLResponse(status_code=404)
        

    @app.post("/infections")
    def create_infection(infection: dict):
        if response := requests.post(url + "infections").status_code == 200:
            response = requests.post(url + "infections", json=infection)
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.post("/reports")
    def create_report(report: dict):
        if response := requests.post(url + "reports").status_code == 200:
            response = requests.post(url + "reports", json=report)
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.patch("/countries/{country_id}")
    def update_country(country_id: int, country: dict):
        if response := requests.patch(url + f"countries/{country_id}").status_code == 200:
            response = requests.patch(url + f"countries/{country_id}", json=country)
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.patch("/pandemics/{pandemic_id}")
    def update_pandemic(pandemic_id: int, pandemic: dict):
        if response := requests.patch(url + f"pandemics/{pandemic_id}").status_code == 200:
            response = requests.patch(url + f"pandemics/{pandemic_id}", json=pandemic)
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.patch("/infections/{infection_id}")
    def update_infection(infection_id: int, infection: dict):
        if response := requests.patch(url + f"infections/{infection_id}").status_code == 200:
            response = requests.patch(url + f"infections/{infection_id}", json=infection)
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.patch("/reports/{report_id}")
    def update_report(report_id: int, report: dict):
        if response := requests.patch(url + f"reports/{report_id}").status_code == 200:
            response = requests.patch(url + f"reports/{report_id}", json=report)
            return response.json()
        else:
            return HTMLResponse(status_code=404)
        
    @app.delete("/countries/{country_id}")
    def delete_country(country_id: int):
        if response := requests.delete(url + f"countries/{country_id}").status_code == 200:
            response = requests.delete(url + f"countries/{country_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.delete("/pandemics/{pandemic_id}")
    def delete_pandemic(pandemic_id: int):
        if response := requests.delete(url + f"pandemics/{pandemic_id}").status_code == 200:
            response = requests.delete(url + f"pandemics/{pandemic_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)
        
    @app.delete("/infections/{infection_id}")
    def delete_infection(infection_id: int):
        if response := requests.delete(url + f"infections/{infection_id}").status_code == 200:
            response = requests.delete(url + f"infections/{infection_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)

    @app.delete("/reports/{report_id}")
    def delete_report(report_id: int):
        if response := requests.delete(url + f"reports/{report_id}").status_code == 200:
            response = requests.delete(url + f"reports/{report_id}")
            return response.json()
        else:
            return HTMLResponse(status_code=404)
        
except Exception as e:
    print(f"An error occurred: {e}")