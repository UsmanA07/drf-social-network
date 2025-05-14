from apps.user.dto.user_dto import UserRegisterDTO


def test_user_register(service, mock_repo):
    dto = UserRegisterDTO(username="testuser",
                          email="test@example.com",
                          password="securepass",
                          first_name=None,
                          last_name=None,
                          phone=None)
    service.execute(dto)
    mock_repo.user_register.assert_called_once_with(dto)
