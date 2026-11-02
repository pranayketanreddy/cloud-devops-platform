
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


def test_invalid_url_returns_404():
    client = app.test_client()

    response = client.get("/invalid")

    assert response.status_code == 404
    assert response.json == {
        "error": "Resource not found"
    }


def test_logger_is_configured():
    from app.main import logger

    assert logger.name == "cloud_devops"
    assert logger.level == 20

