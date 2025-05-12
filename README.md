### FAST API
[Documentation de FastAPI](https://fastapi.tiangolo.com/)

### Installation Du Projet
1. Cloner le dépôt
```bash
git clone https://github.com/MSPRProject/ApiPython.git
cd ApiPython
```

2. Créer un environement virtuel python

Linux : 
```bash
python3 -m venv nom_du_venv
source venv/bin/activate
```
Windows : 
```bash
python3 -m venv nom_du_venv
venv\Scripts\activate
```
3. Installer les dépendances
```bash
pip install -r requirements.txt
``` 

4. Modifier le [.env.example](.env.example)
```bash 
BEARER_TOKEN = "your_bearer_token"
```

5. Lancer le serveur FastAPI
```bash
py start.py
```


### Route de l'API    
GET : 
```bash
- /prompt
```

### Arborescence de l'API
Structure de l'api : 
```bash
APIPYTHON/
├──.env
├──main.py
├──requirements.txt
├──start.py
```