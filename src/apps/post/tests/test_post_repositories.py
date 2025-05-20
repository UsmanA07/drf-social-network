import pytest

from apps.post.repositories.post_repositories import *
from apps.post.dto.post_dto import *
from apps.post.models import Post
from apps.user.models import ProfileUser

@pytest.mark.django_db
def test_get_all():
    user = ProfileUser.objects.create_user(
        username="testuser",
        first_name="Test",
        last_name="User",
        phone="+1234567890",
        email="test@example.com",
        password="securepass"
    )
    Post.objects.create(id=1, user=user, title='t', text='tt', published='1')
    Post.objects.create(id=2, user=user, title='t1', text='tt1', published='2')

    repo = ImplPostRepository()
    posts = repo.get_all()

    assert len(posts) == 2
    assert posts[0].title == 't'
    assert posts[1].title == 't1'



@pytest.mark.django_db
def test_post_create():
    user = ProfileUser.objects.create_user(
        username="testuser",
        first_name="Test",
        last_name="User",
        phone="+1234567890",
        email="test@example.com",
        password="securepass"
    )
    repo = ImplPostRepository()
    dto = PostCreateDTO(user=user, title='t', text='tt')

    post = repo.post_create(dto)

    assert Post.objects.count() == 1
    assert post.title == "t"
    assert post.text == "tt"


@pytest.mark.django_db
def test_post_get_by_id():
    user = ProfileUser.objects.create_user(
        username="testuser",
        first_name="Test",
        last_name="User",
        phone="+1234567890",
        email="test@example.com",
        password="securepass"
    )
    post = Post.objects.create(id=1, user=user, title='t', text='tt', published='1')

    repo = ImplPostRepository()
    result = repo.get_by_id(post.id)

    assert result.title == "t"


@pytest.mark.django_db
def test_post_update_by_id():
    user = ProfileUser.objects.create_user(
        username="testuser",
        first_name="Test",
        last_name="User",
        phone="+1234567890",
        email="test@example.com",
        password="securepass"
    )
    post = Post.objects.create(id=1, user=user, title='t', text='tt', published='1')

    repo = ImplPostRepository()
    update_dto = PostUpdateDTO(title='tu', text='ttu', user=user)
    updated_post = repo.update_by_id(post.id, update_dto)

    assert updated_post.title == "tu"
    assert updated_post.text == "ttu"


@pytest.mark.django_db
def test_post_delete_by_id():
    user = ProfileUser.objects.create_user(
        username="testuser",
        first_name="Test",
        last_name="User",
        phone="+1234567890",
        email="test@example.com",
        password="securepass"
    )
    post = Post.objects.create(id=1, user=user, title='t', text='tt', published='1')

    repo = ImplPostRepository()
    result = repo.delete_by_id(post.id)

    assert result is True
    assert Post.objects.count() == 0