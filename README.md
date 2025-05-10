### FAST API

    Documentation de FastAPI[FastAPI Docs](https://fastapi.tiangolo.com/)

### Installation Du Projet

    1. Cloner le dépôt

            git clone https://github.com/MSPRProject/ApiPython.git
            cd ApiPython
     
    2. Créer un environement virtuel python

            python3 -m venv venv
            source venv/bin/activate
      
    3. Installer les dépendances

            pip install -r requirements.txt
        

    4. Lancer le serveur FastAPI

            py start.py
        

### Route de l'API

    1. GET :    
        - /countries
        - /countries/{id}
        - /pandemics
        - /pandemics/{id}
        - /infections
        - /infections/{id}
        - /reports
        - /reports/{id}
        - /infections/pandemics/{id}
        - /infections/countries/{id}
        - /reports/countries/{id}
        - /reports/{date}
    
    2. POST
        - /countries
        - /pandemics
        - /infections
        - /reports
    
    3. PATCH
        - /countries/{id}
        - /pandemics/{id}
        - /infections/{id}
        - /reports/{id}
    
    4. DELETE
        - /countries/{id}
        - /pandemics/{id}
        - /infections/{id}
        - /reports/{id}
