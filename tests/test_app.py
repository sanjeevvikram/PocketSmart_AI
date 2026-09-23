from fastapi.testclient import TestClient

from app.main import app


def test_health():
    with TestClient(app) as client:
        response = client.get("/health")

        assert response.status_code == 200
        assert response.json()["status"] == "ok"


def register_login(client):
    email = "test@example.com"

    register_response = client.post(
        "/api/auth/register",
        json={
            "email": email,
            "password": "Test@123",
        },
    )

    # Registration may already exist from a previous test run.
    assert register_response.status_code in (200, 409)

    login_response = client.post(
        "/api/auth/login",
        json={
            "email": email,
            "password": "Test@123",
        },
    )

    assert login_response.status_code == 200


def test_home_requires_auth():
    with TestClient(app) as client:
        response = client.post(
            "/api/generate-home",
            json={
                "budget": 10000,
                "rooms": ["Living Room"],
                "items": [
                    {
                        "name": "light",
                        "quantity": 1,
                    }
                ],
                "style": "modern",
                "notes": "",
            },
        )

        assert response.status_code == 401


def test_home_fallback():
    with TestClient(app) as client:
        register_login(client)

        response = client.post(
            "/api/generate-home",
            json={
                "budget": 10000,
                "rooms": ["Living Room"],
                "items": [
                    {
                        "name": "light",
                        "quantity": 1,
                    }
                ],
                "style": "modern",
                "notes": "",
            },
        )

        assert response.status_code == 200

        data = response.json()

        assert data["planner"] == "home"
        assert data["estimated_total"] <= 10000