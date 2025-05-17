import pytest
from unittest.mock import MagicMock
from rest_framework.test import APIClient

from apps.comment.models import Comment
from apps.comment.services.comment_services import CommentServices
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


@pytest.fixture
def comment(post, user):
    return Comment.objects.create(user=user, post=post, text='c', published='1')


@pytest.fixture
def mock_repo():
    return MagicMock()


@pytest.fixture
def service(mock_repo):
    return CommentServices(mock_repo)
