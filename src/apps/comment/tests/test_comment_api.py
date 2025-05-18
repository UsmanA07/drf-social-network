import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_comment(client, comment, post):
    url = f"/api/v1/post-detail/{post.id}"
    response = client.get(url)
    value = response.data["comments"][0].get('text')
    assert response.status_code == 200
    assert value == comment.text


@pytest.mark.django_db
def test_create_comment(client, comment, post, user):
    url = reverse('comment:comment-create', args=[post.id])
    data = {'text': 'cc', 'post': comment.post, 'user': comment.user}
    response = client.post(url, data)

    assert response.status_code == 201
    assert comment.text == 'c'


def test_delete_comment(client, comment, post, user):
    url = reverse('comment:comment-delete', args=[comment.id])
    response = client.delete(url)
    assert response.status_code == 204

@pytest.mark.django_db
def test_update_comment(client, comment, post, user):
    url = reverse('comment:comment-update', args=[comment.id])
    data = {'text': 'cc'}
    response = client.put(url, data)

    assert response.status_code == 201