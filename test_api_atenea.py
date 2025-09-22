import requests

def test_youtube_api():
    """Test para verificar API de YouTube de Atenea Conocimientos"""
    
    # URL y headers del cURL
    url = "https://www.googleapis.com/youtube/v3/channels"
    
    params = {
        'part': 'statistics',
        'id': 'UCg1DTFXqx5qnBLlXUGbOnjA',
        'key': 'AIzaSyA-t1jTDKUTZkYs6AgSZJmTIFVITM4mXCk'
    }
    
    headers = {
        'accept': '*/*',
        'origin': 'https://ateneaconocimientos.com',
        'referer': 'https://ateneaconocimientos.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
    }
    
    # Hacer la petición
    response = requests.get(url, params=params, headers=headers)
    
    # Verificaciones básicas
    assert response.status_code == 200
    
    # Verificar que devuelve JSON
    data = response.json()
    
    # Verificar estructura de respuesta de YouTube API
    assert 'items' in data
    assert len(data['items']) > 0
    assert 'statistics' in data['items'][0]