import sys, os
import pytest

# thêm project root vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from routes import tasks as tasks_mod

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({"TESTING": True})
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def reset_tasks(monkeypatch):
    monkeypatch.setattr(tasks_mod, "tasks", [])
