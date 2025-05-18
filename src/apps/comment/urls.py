from django.urls import path, include

from api.v1.comment.views import *

app_name = 'comment'

urlpatterns = [
    path('comment/<int:post_id>/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('comment/<int:comment_id>/update/', CommentUpdateView.as_view(), name='comment-update'),
]
