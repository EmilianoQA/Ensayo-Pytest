# Pytest-API Demo

Este proyecto es un ejemplo sencillo de automatización de pruebas con **Pytest**, orientado a validar el funcionamiento de APIs y mostrar la integración con **GitHub Actions** para ejecución continua.

## Características principales
- Pruebas básicas de API utilizando `pytest` y `requests`.
- Integración con **GitHub Actions** para ejecución automática de tests en cada *push* o *pull request*.
- Estructura simple y clara, pensada para demostración y como base de futuros proyectos.

## Estructura del proyecto
- `test_api_atenea.py` → Pruebas de API Atenea.  
- `test_api_playwright.py` → Pruebas con Playwright.  
- `test_login_atenea.py` → Pruebas de autenticación.  
- `.github/workflows/tests.yml` → Definición del pipeline de CI/CD.  

## Ejecución local
```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias
pip install pytest requests

# Ejecutar tests
pytest -v
