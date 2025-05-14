import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate

from api.v1.post.views import PostListView, PostDetailView
from apps.post.models import Post


@pytest.mark.django_db
def test_get_post_list(user):
    factory = APIRequestFactory()
    view = PostListView.as_view()
    request = factory.get('/api/v1/posts/')
    force_authenticate(request, user=user)

    response = view(request)
    assert response.status_code == 200
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_create_post(user):
    factory = APIRequestFactory()
    view = PostListView.as_view()
    data = {"title": "Test Title", "text": "Test text content"}
    request = factory.post('/api/v1/posts/', data, format='json')
    force_authenticate(request, user=user)

    response = view(request)
    assert response.status_code == 201
    assert Post.objects.filter(title="Test Title").exists()


@pytest.mark.django_db
def test_get_post_detail(client, post):
    url = f"/api/v1/post-detail/{post.id}"
    response = client.get(url)
    assert response.status_code == 200
    assert response.data["title"] == post.title == 't'


@pytest.mark.django_db
def test_delete_post(client, post):
    url = f"/api/v1/post-detail/{post.id}"
    response = client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_nonexistent_post(client):
    url = f"/api/v1/post-detail/9999"
    response = client.delete(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_patch_post(client, post):
    url = f"/api/v1/post-detail/{post.id}"
    data = {"title": "Updated Title"}
    response = client.patch(url, data)
    assert response.status_code == 203
