from django.urls import path, include
from api.v1.post.views import PostListView, PostDetailView

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view()),
    path('post-detail/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
]
