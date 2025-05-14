import pytest
from unittest.mock import MagicMock
from rest_framework.test import APIClient

from apps.user.models import ProfileUser
from apps.user.services.user_services import UserRegister

User = ProfileUser

@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser",
                                    email="test@example.com",
                                    password="securepass")


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def mock_repo():
    return MagicMock()


@pytest.fixture
def service(mock_repo):
    return UserRegister(mock_repo)
