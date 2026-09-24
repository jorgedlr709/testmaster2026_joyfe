import pytest

from app import crear_app


@pytest.fixture
def db_path(tmp_path):
    return tmp_path / "test.db"


@pytest.fixture
def app(db_path):
    application = crear_app(str(db_path))
    application.config.update(TESTING=True)
    return application


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def token(client):
    client.post("/registro", json={"username": "ana", "password": "secreto"})
    response = client.post("/login", json={"username": "ana", "password": "secreto"})
    return response.get_json()["token"]


@pytest.fixture
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}
