from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.post.serializers import *
from apps.post.dto.post_dto import PostCreateDTO, PostUpdateDTO
from apps.post.services.post_services import PostServices
from apps.post.repositories.post_repositories import ImplPostRepository
from api.v1.permissions import IsOwnerOrReadOnly


# noinspection PyUnusedLocal
class PostListView(APIView):
    permission_classes = [permissions.AllowAny, IsOwnerOrReadOnly]

    @staticmethod
    def get(request):
        post_services = PostServices(ImplPostRepository())
        posts = post_services.post_list()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = PostCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        post_dto = PostCreateDTO(
            user=request.user,
            title=serializer.validated_data['title'],
            text=serializer.validated_data['text'],
        )
        post_services = PostServices(ImplPostRepository())
        post_services.post_create(post_dto)
        return Response(status=201)


# noinspection PyUnusedLocal
class PostDetailView(APIView):
    permission_classes = [permissions.AllowAny, IsOwnerOrReadOnly]

    @staticmethod
    def get(request, post_id):
        post_services = PostServices(ImplPostRepository())
        post = post_services.post_detail(post_id)
        serializer = PostDetailSerializers(post)
        return Response(serializer.data)

    def post(self, request, post_id):
        post_services = PostServices(ImplPostRepository())
        post_services.post_like(post_id, request.user)
        return Response(status=201)

    def delete(self, request, post_id):
        post_detail_services = PostServices(ImplPostRepository())
        post = post_detail_services.post_detail(post_id)
        self.check_object_permissions(request, post)

        post_services = PostServices(ImplPostRepository())
        post_delete = post_services.post_delete(post_id)
        if not post_delete:
            return Response(status=404)
        return Response(status=204)

    def patch(self, request, post_id):
        serializer = PostUpdateSerializers(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        post_detail_services = PostServices(ImplPostRepository())
        post = post_detail_services.post_detail(post_id)
        self.check_object_permissions(request, post)

        post_dto = PostUpdateDTO(
            user=post.user,
            title=serializer.validated_data.get('title'),
            text=serializer.validated_data.get('text'),

        )
        post_services = PostServices(ImplPostRepository())
        post_services.post_update(post_id, post_dto)

        return Response(status=203)
