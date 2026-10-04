from fastapi.testclient import TestClient
from inventory.main import app

client = TestClient(app)


def test_summary():
    payload = client.post("/analyze", json={"rows": [{'kind': 'gke', 'monthly': 40}, {'kind': 'gke', 'monthly': 60}, {'kind': 'gcs', 'monthly': 50}]}).json()
    assert payload["mean"] == 50.0
    assert payload["by_kind"]["gke"]


def test_empty_is_refused():
    assert client.post("/analyze", json={"rows": []}).status_code == 422
