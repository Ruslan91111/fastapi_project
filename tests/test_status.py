from fastapi.testclient import TestClient
from ..fastapi_project.main import app
from ..fastapi_project.settings import settings


def test_answer():
    """ Test main page. """
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}