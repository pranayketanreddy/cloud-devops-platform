
from app.main import app


def test_homepage_returns_200():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["application"] == "Cloud DevOps Platform"


def test_health_endpoint_returns_200():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
