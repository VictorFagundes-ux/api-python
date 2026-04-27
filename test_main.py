from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_status():
    response = client.get("/api")
    assert response.status_code == 200

def test_api_response():
    response = client.get("/api")
    assert response.json() == {"mensagem": "Hello World"}

def test_teste_status():
    response = client.get("/teste")
    assert response.status_code == 200

def test_teste_response():
    response = client.get("/teste")
    assert response.json() == {"mensagem": "testando"}

def test_rota_invalida():
    response = client.get("/rota-inexistente")
    assert response.status_code == 404
