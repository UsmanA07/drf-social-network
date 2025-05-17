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
    url = reverse('comment:comments-list', args=[post.id])
    data = {'text': 'cc', 'post': comment.post, 'user': comment.user}
    response = client.post(url, data)

    print(response)
    assert response.status_code == 201

    assert comment.text == 'c'
