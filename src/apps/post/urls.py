from django.urls import path, include
from api.v1.post.views import PostListView, PostDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view()),
    path('post-detail/<int:pk>', PostDetailView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
