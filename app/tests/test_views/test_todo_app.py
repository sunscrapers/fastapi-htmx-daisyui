from typing import List

from app.db import TodoItem


def test_todo_view(client):
    response = client.get("/todo")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Todo App" in response.text


def test_todo_list(client):
    response = client.get("/todo/list")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

    assert "Task1" in response.text
    assert "Task2" in response.text


def test_todo_add(client, db, csrftoken):
    # No CSRFToken generated and set
    client.cookies.pop("fastcsrftoken")
    response = client.post("/todo/add", data={"value": "New Todo Item"})
    assert response.status_code == 403
    assert len(db.get_todo_items()) == 2

    # CSRFToken mismatch
    client.cookies.set("fastcsrftoken", csrftoken)
    response = client.post(
        "/todo/add",
        data={"value": "New Todo Item"},
        headers={"x-fastcsrftoken": "123"},
    )
    assert response.status_code == 403
    assert len(db.get_todo_items()) == 2

    # CSRFToken correct
    response = client.post(
        "/todo/add",
        data={"value": "New Todo Item"},
        headers={"x-fastcsrftoken": csrftoken},
    )
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

    assert len(db.get_todo_items()) == 3
    assert "Task1" in response.text
    assert "Task2" in response.text
    assert "New Todo Item" in response.text


def test_todo_remove(client, db, csrftoken):
    todo_items: List[TodoItem] = db.get_todo_items()
    assert len(todo_items) == 2

    response = client.post(
        "/todo/remove",
        data={"item_id": str(todo_items[0].id)},
        headers={"x-fastcsrftoken": csrftoken},
    )

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert len(db.get_todo_items()) == 1
    assert "Task1" not in response.text
    assert "Task2" in response.text


def test_todo_clear(client, db, csrftoken):
    assert len(db.get_todo_items()) == 2

    response = client.post(
        "/todo/clear",
        headers={"x-fastcsrftoken": csrftoken},
    )

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert len(db.get_todo_items()) == 0
