import pytest
from unittest.mock import MagicMock

from apps.post.services.post_services import *
from apps.post.dto.post_dto import *

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def service(mock_repo):
    return PostServices(mock_repo)

def test_post_list(service, mock_repo):
    service.post_list()
    mock_repo.get_all.assert_called_once()

def test_post_create(service, mock_repo):
    dto = PostCreateDTO(title="t", text="c", user='Usman')
    print(dto)
    service.post_create(dto)
    mock_repo.post_create.assert_called_once_with(dto)

def test_post_detail(service, mock_repo):
    post_id = 1
    service.post_detail(post_id)
    mock_repo.get_by_id.assert_called_once_with(post_id)

def test_post_delete(service, mock_repo):
    post_id = 1
    service.post_delete(post_id)
    mock_repo.delete_by_id.assert_called_once_with(post_id)

def test_post_update(service, mock_repo):
    post_id = 1
    dto = PostUpdateDTO(title="t", text=None)
    service.post_update(post_id, dto)
    mock_repo.update_by_id.assert_called_once_with(post_id, dto)

# test_post_update(service, mock_repo)