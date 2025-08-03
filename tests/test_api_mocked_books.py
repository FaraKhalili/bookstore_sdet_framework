import pytest
import requests
import responses


@responses.activate
def test_mocked_get_books():
    url = "https://api.example.com/books"

    responses.add(
        method=responses.GET,
        url=url,
        json=[{"title": "Mock Book", "author": "Fake Author", "price": 10}],
        status=200
    )

    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["title"] == "Mock Book"

@responses.activate
def test_mocked_404():
    url = "https://api.example.com/notfound"

    responses.add(
        method=responses.GET,
        url=url,
        status=404
    )

    response = requests.get(url)
    assert response.status_code == 404

@responses.activate
def test_mocked_timeout():
    url = "https://api.example.com/timeout"

    responses.add(
        method=responses.GET,
        url=url,
        body=requests.exceptions.Timeout("Server took too long"),
    )

    with pytest.raises(requests.exceptions.Timeout):
        requests.get(url, timeout=1)

@responses.activate
def test_mocked_invalid_json():
    url = "https://api.example.com/badjson"

    responses.add(
        method=responses.GET,
        url=url,
        body="This is not JSON!",
        status=200,
        content_type="application/json"
    )

    with pytest.raises(ValueError):
        requests.get(url).json()

