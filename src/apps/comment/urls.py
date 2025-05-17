from django.urls import path, include

from api.v1.comment.views import CommentListView

app_name = 'comment'

urlpatterns = [
    path('post/<int:post_id>/comments/', CommentListView.as_view()),
]
2