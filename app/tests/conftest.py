import uuid

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.db import TodoItem
from app.db import db_handler


@pytest.fixture
def app() -> FastAPI:
    from app.main import get_application

    return get_application()


@pytest.fixture()
def client(app):
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def db():
    db_handler.clear_todo_items()
    db_handler.todo_items = [
        TodoItem(
            id=uuid.UUID("3bd151d9-353f-4aa9-8ed9-28b4c6bd8f6b"),
            value="Task1",
        ),
        TodoItem(
            id=uuid.UUID("dbe6d239-ff77-405a-8479-8c938be770a9"),
            value="Task2",
        ),
    ]
    return db_handler
