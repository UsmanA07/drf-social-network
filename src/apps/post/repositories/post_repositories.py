import redis
from django.conf import settings
from apps.post.dto.post_dto import (
    PostListDTO,
    PostCreateDTO,
    PostDetailDTO,
    PostUpdateDTO,
)
from apps.post.models import Post
from abc import ABC, abstractmethod


class PostRepository(ABC):
    @abstractmethod
    def get_by_id(self, post_id: int) -> PostDetailDTO:
        pass

    @abstractmethod
    def get_all(self) -> list[PostListDTO]:
        pass

    @abstractmethod
    def post_create(self, post_dto: PostCreateDTO) -> PostCreateDTO:
        pass

    @abstractmethod
    def update_by_id(
            self, post_id: int, post_dto: PostUpdateDTO
    ) -> PostUpdateDTO | None:
        pass

    @abstractmethod
    def delete_by_id(self, post_id: int) -> bool:
        pass


class ImplPostRepository(PostRepository):
    def update_by_id(self, post_id: int, post_dto):
        try:
            post = Post.objects.get(id=post_id)
            if post_dto.title is not None:
                post.title = post_dto.title
            if post_dto.text is not None:
                post.text = post_dto.text
            post.save()
            return PostUpdateDTO(title=post.title, text=post.text, user=post_dto.user)
        except Post.DoesNotExist:
            return None

    def delete_by_id(self, post_id: int):
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return True
        except Post.DoesNotExist:
            return False

    def post_create(self, post_dto: PostCreateDTO):
        post = Post.objects.create(
            user=post_dto.user, title=post_dto.title, text=post_dto.text
        )

        return PostCreateDTO(title=post.title, text=post.text, user=post.user)

    def get_by_id(self, post_id: int):
        post = Post.objects.get(id=post_id)
        r = redis.Redis(host=settings.REDIS_HOST,
                        port=settings.REDIS_PORT,
                        db=settings.REDIS_DB)

        total_views = r.incr(f'post:{post.id}:views')
        return PostDetailDTO(
            id=post.id,
            user=post.user,
            title=post.title,
            text=post.text,
            published=post.published,
            posts_comment=post.posts_comment,
            like_count=post.like.all().count(),
            like=post.like,
            views_count=total_views,
        )

    def get_all(self):
        posts = Post.objects.all()
        return [
            PostListDTO(
                id=post.id,
                user=post.user,
                title=post.title,
                text=post.text,
                published=post.published,
            )
            for post in posts
        ]
