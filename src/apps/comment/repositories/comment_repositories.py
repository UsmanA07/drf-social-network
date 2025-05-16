from apps.comment.dto.comment_dto import CommentListDTO
from apps.comment.models import Comment
from abc import ABC, abstractmethod

from apps.post.models import Post


class CommentRepository(ABC):
    @abstractmethod
    def get_all(self, post_id) -> list[CommentListDTO]:
        pass


class DjangoCommentRepository(CommentRepository):
    def get_all(self, post_id):
        post1 = Post.objects.get(pk=post_id)
        comments = Comment.objects.filter(post=post_id)
        print(comments)
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
