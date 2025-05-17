from apps.comment.dto.comment_dto import CommentListDTO, CommentCreateDTO
from apps.comment.models import Comment
from abc import ABC, abstractmethod

from apps.post.models import Post


class CommentRepository(ABC):
    @abstractmethod
    def get_all(self, post_id) -> list[CommentListDTO]:
        pass

    @abstractmethod
    def comment_create(self, comment_dto, post_id,) -> CommentCreateDTO:
        pass


class ImplCommentRepository(CommentRepository):
    def get_all(self, post_id):
        comments = Comment.objects.filter(post=post_id)
        return [
            CommentListDTO(
                id=comment.id,
                user=comment.user,
                post=comment.post,
                text=comment.text,
                published=comment.published,
            )
            for comment in comments
        ]

    def comment_create(self, comment_dto: CommentCreateDTO, post_id):
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(user=comment_dto.user, post=post, text=comment_dto.text)
        return CommentCreateDTO(user=comment.user, post=comment.post, text=comment.text)
