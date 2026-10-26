from fastapi.testclient import TestClient

from pr_impact_analyzer.api import app

client = TestClient(app)


def test_health_returns_200_and_ok_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
