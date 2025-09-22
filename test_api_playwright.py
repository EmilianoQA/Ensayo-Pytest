import requests

def test_api_simple_get():
    response = requests.get ("https://playwright.dev/")
    assert response.status_code == 200
    data = response.json
   

   