
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["application"] == "devops-python-app"

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "UP"

def test_ready():
    client = app.test_client()
    response = client.get("/ready")
    assert response.status_code == 200

def test_metrics():
    client = app.test_client()
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"app_http_requests_total" in response.data
