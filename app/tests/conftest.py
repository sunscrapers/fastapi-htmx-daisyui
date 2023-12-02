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


@pytest.fixture
def csrftoken():
    return (
        ".eJwFwe0WQjAAANB36QmsZW0_q6E5sSPVlj8OEfKVIa2n795VzvZL1zpqGybRxKQ5FoflH"
        "cZoVhqnFLYB043ghtVWhNmXGmQNI_yUdD7WJseGytzNqdKIZ1fLJNCmTrSGw21m9mf0QN2"
        "LxA2K-Hx_ph5_Fa9BipEus-dY1Y98HKB25WN3kz6IDr-z9CBl135P8zfyhfsFdEp7iGtVH"
        "g2IIrz6A5_7OQY.6lMN1TAYgTA5y_ZgLL0b4wpQFFA"
    )


@pytest.fixture()
def client(app, csrftoken):
    with TestClient(app) as test_client:
        test_client.cookies.set("fastcsrftoken", csrftoken)
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
