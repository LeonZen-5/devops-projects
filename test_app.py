import pytest
import app as app_module


@pytest.fixture
def client():
    app_module.tasks.clear()
    app_module.next_id = 1
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as test_client:
        yield test_client


def test_list_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task_returns_201(client):
    response = client.post("/tasks", json={"description": "buy milk"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["description"] == "buy milk"
    assert data["done"] is False
    assert data["id"] == 1


def test_create_task_missing_description_returns_400(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_list_returns_created_task(client):
    client.post("/tasks", json={"description": "study"})
    response = client.get("/tasks")
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["description"] == "study"


def test_delete_existing_task_returns_204(client):
    client.post("/tasks", json={"description": "buy milk"})
    response = client.delete("/tasks/1")
    assert response.status_code == 204


def test_delete_missing_task_returns_404(client):
    response = client.delete("/tasks/999")
    assert response.status_code == 404
