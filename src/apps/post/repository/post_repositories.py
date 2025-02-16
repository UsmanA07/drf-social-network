from apps.post.dto.post_dto import PostListDTO, PostCreateDTO
from apps.post.models import Post


class PostRepository:
    def get_all(self):
        posts = Post.objects.all()
        return [
            PostListDTO(
                id=post.id,
                user=post.user,
                title=post.title,
                text=post.text,
                published=post.published
            )
            for post in posts
        ]

    def post_create(self, post_dto: PostCreateDTO):
        post = Post.objects.create(
            user=post_dto.user,
            title=post_dto.title,
            text=post_dto.text
        )

        return PostCreateDTO(
            title=post.title,
            text=post.text,
            user=post.user
        )
