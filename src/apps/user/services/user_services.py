from apps.user.dto.user_dto import UserRegisterDTO


class UserRegister:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_dto: UserRegisterDTO):
        return self.repository.user_register(user_dto)
