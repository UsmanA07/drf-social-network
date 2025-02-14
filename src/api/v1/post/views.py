from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from api.v1.post.serializers import *
from apps.post.dto.post_dto import PostListDTO
from apps.post.services.post_services import PostServices

from django.contrib.auth import get_user_model

from apps.user.models import ProfileUser


class PostListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # post_dto = PostListDTO(
        #     id=None,
        #     user=serializers.validated_data['user'],
        #     title=serializers.validated_data['title'],
        #     content=serializers.validated_data['content'],
        #     published=serializers.validated_data['published'],
        # )
        print('Определяем экземпляр')
        post_services = PostServices()
        print('Вызываем объект')
        posts = post_services.post_list()
        serializers = PostListSerializer(posts, many=True)
        print('Отправляем объект', serializers.data)
        return Response(serializers.data)

    def post(self, request):
        pass


class PostDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        pass

    def delete(self, pk):
        pass

    def patch(self, request, pk):
        pass
