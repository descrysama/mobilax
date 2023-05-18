import requests
import json

def login():
    login_url = "https://www.mobilax.fr/api?model=Auth&action=connect&controller=Auth"
    login_payload = {
        "email": "louis.lantiez4@icloud.com",
        "password": "Google59"
    }
    print(json.dumps({'MOBILAX': 'going into login process...'}))
    login_response = requests.post(login_url, data=login_payload)

    if login_response.status_code == 200:
        print(json.dumps({'MOBILAX': 'Login successful'}))
        auth_token = login_response.json()
        token = auth_token['auth'].get('token')
        
        return token

    else:
        # La connexion a échoué
        print("Échec de la connexion.")