import json

import responses
import requests

@responses.activate
def test_mocked_books_with_query_param():
    url = "https://api.example.com/books?category=fiction"

    responses.add(
        method=responses.GET,
        url=url,
        json=[{"title": "Mocked Fiction", "category": "fiction"}],
        status=200
    )

    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()[0]["category"] == "fiction"
@responses.activate
def test_mocked_auth_header():
    url = "https://api.example.com/secure"

    responses.add(
        method=responses.GET,
        url=url,
        match=[responses.matchers.header_matcher({
            "Authorization": "Bearer testtoken123"
        })],
        json={"access": "granted"},
        status=200
    )

    headers = {"Authorization": "Bearer testtoken123"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert response.json()["access"] == "granted"
def book_callback(request):
    payload = [{"title": f"Book {i}"} for i in range(1, 4)]
    return (200, {"Content-Type": "application/json"}, str(payload))

@responses.activate
def test_mocked_books_callback():
    responses.add_callback(
        responses.GET,
        "https://api.example.com/dynamic-books",
        callback=book_callback
    )

    response = requests.get("https://api.example.com/dynamic-books")
    assert response.status_code == 200
@responses.activate
def test_mocked_with_auth_header():
    url = "https://api.example.com/secure"

    responses.add(
        method=responses.GET,
        url=url,
        match=[
            responses.matchers.header_matcher({
                "Authorization": "Bearer my-secret-token"
            })
        ],
        json={"message": "Access granted"},
        status=200
    )

    headers = {"Authorization": "Bearer my-secret-token"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json()["message"] == "Access granted"

    @responses.activate
    def test_mocked_with_query_params():
        url = "https://api.example.com/books?genre=fiction"

        responses.add(
            method=responses.GET,
            url=url,
            json=[{"title": "Mocked Fiction Book", "genre": "fiction"}],
            status=200
        )

        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()[0]["genre"] == "fiction"

    def dynamic_books_callback(request):
        books = [{"title": f"Book {i}", "price": 10 * i} for i in range(1, 4)]
        return (200, {"Content-Type": "application/json"}, json.dumps(books))

    @responses.activate
    def test_mocked_with_callback():
        url = "https://api.example.com/dynamic-books"

        responses.add_callback(
            responses.GET,
            url,
            callback=dynamic_books_callback,
            content_type="application/json"
        )

        response = requests.get(url)
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert response.json()[0]["title"] == "Book 1"
