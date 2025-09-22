import requests

def test_atenea_login_simple():
    url = "https://ateneaconocimientos.com/api/students/login"
    
    headers = {
        'content-type': 'application/json'
    }
    
    login_data = {
        "email": "qaatyourservice@gmail.com", 
        "password": "Atenea2025"
    }
    
    response = requests.post(url, json=login_data, headers=headers)
    assert response.status_code == 200

def test_atenea_login_failed():
    url = "https://ateneaconocimientos.com/api/students/login"
    
    headers = {
        'content-type': 'application/json'
    }
    
    login_data = {
        "email": "qaatyourservice@gmail.com", 
        "password": "Atenea202"
    }
    
    response = requests.post(url, json=login_data, headers=headers)
    assert response.status_code == 401