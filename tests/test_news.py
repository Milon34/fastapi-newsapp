import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.auth import create_access_token

client = TestClient(app)


def get_test_token():
    return create_access_token(data={"sub": "test_client"})


@pytest.fixture
def token_header():
    token = get_test_token()
    return {"Authorization": f"Bearer {token}"}


def test_get_all_news(token_header):
    response = client.get("/news?page=1&limit=10", headers=token_header)
    assert response.status_code == 200
    data = response.json()
    assert "articles" in data
    assert isinstance(data["articles"], list)


def test_get_headlines_by_country(token_header):
    response = client.get("/news/headlines/country/us", headers=token_header)
    assert response.status_code == 200
    data = response.json()
    assert "articles" in data
    assert isinstance(data["articles"], list)


def test_save_latest_news(token_header):
    response = client.post("/news/save-latest", headers=token_header)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 3
    if len(data) > 0:
        assert "title" in data[0]
        assert "description" in data[0]


def test_get_headlines_by_source(token_header):
    response = client.get("/news/headlines/source/bbc-news", headers=token_header)
    assert response.status_code == 200
    data = response.json()
    assert "articles" in data
    assert isinstance(data["articles"], list)


def test_get_headlines_filtered(token_header):
    response = client.get(
        "/news/headlines/filter?country=us&source=bbc-news",
        headers=token_header
    )
    assert response.status_code == 200
    data = response.json()
    assert "articles" in data
    assert isinstance(data["articles"], list)


def test_invalid_token():
    invalid_token = "invalid_token"
    response = client.get(
        "/news",
        headers={"Authorization": f"Bearer {invalid_token}"}
    )
    assert response.status_code in [401, 403]


def test_missing_token():
    response = client.get("/news")
    assert response.status_code == 401


def test_invalid_page_size(token_header):
    response = client.get(
        "/news?page=1&limit=0",
        headers=token_header
    )
    assert response.status_code == 422
