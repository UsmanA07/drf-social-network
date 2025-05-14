from unittest.mock import MagicMock

import pytest

from apps.user.services.user_services import UserRegister


@pytest.fixture
def mock_repo():
    return MagicMock()


@pytest.fixture
def service(mock_repo):
    return UserRegister(mock_repo)