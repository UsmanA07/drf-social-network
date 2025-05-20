from apps.comment.dto.comment_dto import *
from apps.comment.models import Comment
from abc import ABC, abstractmethod

from apps.post.models import Post


class CommentRepository(ABC):
    @abstractmethod
    def get_all(self, post_id: int) -> list[CommentListDTO]:
        pass

    @abstractmethod
    def comment_create(self, comment_dto: CommentCreateDTO, post_id: int) -> CommentCreateDTO:
        pass

    @abstractmethod
    def delete_by_id(self, comment_id: int) -> bool:
        pass

    @abstractmethod
    def update_by_id(self, comment_id: int, comment_dto: CommentUpdateDTO) -> CommentUpdateDTO:
        pass

    def get_by_id(self, comment_id: int) -> CommentDetailDTO:
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

    def delete_by_id(self, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return True
        except Post.DoesNotExist:
            return False

    def update_by_id(self, post_id: int, comment_dto):
        try:
            comment = Comment.objects.get(id=post_id)
            comment.text = comment_dto.text
            comment.save()
            print(comment, 'repo')
            return CommentUpdateDTO(text=comment.text, user=comment.user)
        except Post.DoesNotExist:
            return None

    def get_by_id(self, comment_id: int) -> CommentDetailDTO:
        comment = Comment.objects.get(id=comment_id)
        return CommentDetailDTO(
            id=comment.id,
            user=comment.user,
            text=comment.text,
            published=comment.published,
            post=comment.post
        )
