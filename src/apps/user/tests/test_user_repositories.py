import pytest

from apps.post.repositories.post_repositories import DjangoPostRepository
from apps.user.dto.user_dto import UserRegisterDTO
from apps.user.models import ProfileUser
from apps.user.repositories.user_repositories import DjangoUserRepository


@pytest.mark.django_db
def test_user_register():
    dto = UserRegisterDTO(username="testuser",
                          email="test@example.com",
                          password="securepass",
                          first_name="Usman",
                          last_name=".",
                          phone="11111111111")

    repo = DjangoUserRepository()
    user = repo.user_register(dto)

    assert user.username == dto.username
    assert user.phone == dto.phone
    assert ProfileUser.objects.count() == 1
