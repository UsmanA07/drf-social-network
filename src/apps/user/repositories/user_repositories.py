from abc import ABC, abstractmethod

from apps.user.dto.user_dto import UserRegisterDTO
from apps.user.models import ProfileUser


class UserRepository(ABC):
    @abstractmethod
    def user_register(self, user_dto: UserRegisterDTO) -> UserRegisterDTO:
        pass


class DjangoUserRepository(UserRepository):
    def user_register(self, user_dto: UserRegisterDTO):
        user = ProfileUser.objects.create_user(
            username=user_dto.username,
            first_name=user_dto.first_name,
            last_name=user_dto.last_name,
            phone=user_dto.phone,
            email=user_dto.email,
            password=user_dto.password,
        )
        return UserRegisterDTO(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            phone=user.phone,
            email=user.email,
            password=user.password,
        )
