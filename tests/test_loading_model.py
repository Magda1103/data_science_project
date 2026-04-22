from fastapi.testclient import TestClient
from main import app, model_pipline

client = TestClient(app)

def test_home_endpoint():
    """Test if main API is working"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Model loaded"}

def test_model_loaded_properly():
    """Test if model is loaded properly"""
    assert model_pipline is not None
    assert hasattr(model_pipline, "predict")