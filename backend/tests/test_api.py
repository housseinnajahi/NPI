from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculate():
    response = client.post("/api/v1/expressions/calculate/", json={"expression": ["5", "1", "2", "+", "4", "*", "+", "3", "-"]})
    assert response.status_code == 200    
    assert round(response.json()["result"], 2) == 14.0


def test_invalid_operator():
    response = client.post("/api/v1/expressions/calculate/", json={"expression": ["2", "+"]})
    assert response.status_code == 400
    assert "Not enough operands for operator" in response.json()["detail"]


def test_non_numeric():
    response = client.post("/api/v1/expressions/calculate/", json={"expression": ["a", "3", "+"]})
    assert response.status_code == 400
    assert "Invalid non-numeric value" in response.json()["detail"]


def test_division_by_zero():
    response = client.post("/api/v1/expressions/calculate/", json={"expression": ["10", "0", "/"]})
    assert response.status_code == 400
    assert "Division by zero" in response.json()["detail"]


def test_malformed_expression():
    response = client.post("/api/v1/expressions/calculate/", json={"expression": ["2", "3", "+", "4"]})
    assert response.status_code == 400
    assert "Malformed expression" in response.json()["detail"]
