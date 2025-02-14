from apps.post.dto.post_dto import PostListDTO
from apps.post.models import Post


class PostRepository:
    def all_post(self):
        posts = Post.objects.all()
        # print([post for post in posts])
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
