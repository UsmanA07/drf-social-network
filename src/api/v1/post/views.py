from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from api.v1.post.serializers import *
from apps.post.services import post_list, post_create, post_detail, post_delete, post_update

from django.contrib.auth import get_user_model

from apps.user.models import ProfileUser


class PostListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = PostListSerializer(post_list(), many=True)
        return Response(serializer.data)

    def post(self, request):
        post_create(request)
        return Response(status=201)


class PostDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        serializer = PostDetailSerializers(post_detail(pk))
        return Response(serializer.data)

    def delete(self, pk):
        post_delete(pk)
        return Response(status=200)

    def patch(self, request, pk):
        post_update(pk, request)
        return Response(status=200)
