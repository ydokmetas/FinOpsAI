from fastapi.testclient import TestClient

import finopsai.main as main

client = TestClient(main.app)


def test_liveness() -> None:
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}


def test_readiness_when_database_available(monkeypatch) -> None:
    monkeypatch.setattr(main, "database_is_ready", lambda: True)
    response = client.get("/health/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_readiness_when_database_unavailable(monkeypatch) -> None:
    monkeypatch.setattr(main, "database_is_ready", lambda: False)
    response = client.get("/health/ready")
    assert response.status_code == 503
    assert response.json() == {"detail": "Database unavailable"}
