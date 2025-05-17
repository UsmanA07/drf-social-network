from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.comment.repositories.comment_repositories import ImplCommentRepository
from apps.comment.serializers import CommentListSerializer
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
        pass
