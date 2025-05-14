import pytest


@pytest.mark.django_db
def test_user_register_success(client):
    url = f"/auth/register/"  # Убедись, что у тебя задано имя url в urls.py

    data = {
        "first_name": "Usman",
        "last_name": "Akkaev",
        "username": "testuser",
        "phone": "12345678910",
        "email": "usm@gmail.com",
        "password": "1qa2ws3ed/"
    }

    response = client.post(url, data)

    assert response.status_code == 201
