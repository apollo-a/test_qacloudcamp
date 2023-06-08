import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("path, method, expected_status", [
    ("/posts", requests.get, 200),
    ("/posts", requests.post, 201),
    ("/posts/1", requests.delete, 200)
])
def test_api_endpoints(path, method, expected_status):
    url = f"{BASE_URL}{path}"
    response = method(url)
    assert response.status_code == expected_status, f"Failed to call {url}. Got {response.status_code} {response.text}"
