from apps.post.dto.post_dto import PostListDTO, PostCreateDTO, PostDetailDTO, PostUpdateDTO
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

    def get_by_id(self, post_id: int):
        post = Post.objects.get(id=post_id)

        return PostDetailDTO(
            id=post.id,
            user=post.user,
            title=post.title,
            text=post.text,
            published=post.published
        )

    def delete_by_id(self, post_id: int):
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return True
        except Post.DoesNotExist:
            return False

    def update_by_id(self, post_id: int, post_dto):
        try:
            post = Post.objects.get(id=post_id)
            post.title = post_dto.title
            post.text = post_dto.text
            print(post, post.title)
            post.save()
            return PostUpdateDTO(
                title=post.title,
                text=post.text
            )
        except Post.DoesNotExist:
            return None
