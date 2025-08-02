import pytest
import requests

BASE_URL = "https://httpbin.org"

def test_status_200():
    response = requests.get(f"{BASE_URL}/status/200")
    assert response.status_code == 200

def test_get_headers():
    response = requests.get(f"{BASE_URL}/get")
    assert "headers" in response.json()

@pytest.mark.parametrize("status_code", [200, 404, 500])
def test_multiple_status_codes(status_code):
    response = requests.get(f"{BASE_URL}/status/{status_code}")
    assert response.status_code == status_code
