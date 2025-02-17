from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from api.v1.post.serializers import *
from apps.post.dto.post_dto import PostCreateDTO, PostDetailDTO, PostUpdateDTO
from apps.post.services.post_services import PostServices

from django.contrib.auth import get_user_model

from apps.user.models import ProfileUser


class PostListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        post_services = PostServices()
        posts = post_services.post_list()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        post_dto = PostCreateDTO(
            user=request.user,
            title=serializer.validated_data['title'],
            text=serializer.validated_data['text'],
        )
        post_services = PostServices()
        post_services.post_create(post_dto)
        serializer.save()
        return Response(status=201)


class PostDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, post_id):
        post_services = PostServices()
        post = post_services.post_detail(post_id)
        serializer = PostDetailSerializers(post)
        return Response(serializer.data)

    def delete(self, request, post_id):
        post_services = PostServices()
        post = post_services.post_delete(post_id)
        if not post:
            return Response(status=404)
        return Response(status=204)

    def patch(self, request, post_id):
        serializer = PostUpdateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        post_dto = PostUpdateDTO(
            title=serializer.validated_data['title'],
            text=serializer.validated_data['text'],
        )
        print(post_dto.text, 'ducnuiwn')
        post_services = PostServices()
        post_services.post_update(post_id, post_dto)
        print('meivmc', post_services.post_update(post_id, post_dto))
        return Response(status=203)
