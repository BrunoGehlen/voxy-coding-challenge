import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

def test_home_load(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Some text input is required." not in response.data


def test_should_solve_valid_text(client):
    response = client.post(
      '/count',
      data = dict(text="a a a"),
      follow_redirects=True
    )
    
    assert response.status_code == 200
    assert b"Some text input is required." not in response.data
    assert b"You typed 3 words!" in response.data    

def test_should_not_accept_empty_string(client):
    response = client.post(
      '/count',
      data = dict(text=""),
      follow_redirects=True
    )
    
    assert b"Some text input is required." in response.data
