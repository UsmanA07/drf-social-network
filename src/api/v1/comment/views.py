from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.comment.dto.comment_dto import CommentCreateDTO, CommentUpdateDTO
from apps.comment.repositories.comment_repositories import ImplCommentRepository
from apps.comment.serializers import CommentListSerializer, CommentCreateSerializer, \
    CommentUpdateSerializer
from apps.comment.services.comment_services import CommentServices


# noinspection PyUnusedLocal
class CommentView(APIView):
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def get(request, post_id: int):
        comment_services = CommentServices(ImplCommentRepository())
        comments = comment_services.comment_list(post_id)
        serializers = CommentListSerializer(comments, many=True)
        return Response(serializers.data)


class CommentCreateView(APIView):
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def post(request, post_id: int):
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


class CommentDeleteView(APIView):
    permission_classes = [permissions.AllowAny]

    def delete(self, request, comment_id: int):
        comment_services = CommentServices(ImplCommentRepository())
        comment = comment_services.comment_delete(comment_id)
        if not comment:
            return Response(status=404)
        return Response(status=204)


class CommentUpdateView(APIView):
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def put(request, comment_id: int):
        serializer = CommentUpdateSerializer(data=request.data)
        comment_services = CommentServices(ImplCommentRepository())
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        comment_dto = CommentUpdateDTO(text=serializer.validated_data.get('text'))
        print(comment_dto, 'view0')
        comment = comment_services.comment_update(comment_id, comment_dto)
        print(comment, 'view1')
        if not comment:
            return Response(status=404)
        return Response(status=201)
