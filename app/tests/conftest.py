import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture
def app() -> FastAPI:
    from app.main import get_application

    return get_application()


@pytest.fixture()
def client(app):
    with TestClient(app) as test_client:
        yield test_client
