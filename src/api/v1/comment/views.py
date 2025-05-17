from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import serialize

from apps.comment.dto.comment_dto import CommentCreateDTO
from apps.comment.repositories.comment_repositories import ImplCommentRepository
from apps.comment.serializers import CommentListSerializer, CommentCreateSerializer
from apps.comment.services.comment_services import CommentServices


# noinspection PyUnusedLocal
class CommentListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, post_id):
        comment_services = CommentServices(ImplCommentRepository())
        comments = comment_services.comment_list(post_id)
        serializers = CommentListSerializer(comments, many=True)
        return Response(serializers.data)

    def post(self, request, post_id):
        serializer = CommentCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        comment_dto = CommentCreateDTO(
            user=request.user,
            post=post_id,
            text=serializer.validated_data['text'],
        )
        comment_services = CommentServices(ImplCommentRepository())
        comment_services.comment_create(comment_dto, post_id)
        return Response(status=201)
