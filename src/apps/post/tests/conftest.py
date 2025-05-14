import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from apps.post.models import Post
from apps.user.models import ProfileUser

User = ProfileUser


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser",
                                    email="test@example.com",
                                    password="securepass")


@pytest.fixture
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def post(user):
    return Post.objects.create(id=1, user=user, title='t', text='tt', published='1')
