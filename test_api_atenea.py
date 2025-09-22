import requests

def test_api_simple():
    """Test básico para verificar API pública"""
    
    # Usar JSONPlaceholder - API pública sin credenciales
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # Verificaciones básicas
    assert response.status_code == 200
    
    # Verificar que devuelve JSON
    data = response.json()
    
    # Verificar estructura
    assert "id" in data
    assert "title" in data
    assert data["id"] == 1