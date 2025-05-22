from apps.post.dto.post_dto import PostCreateDTO


class PostServices:
    def __init__(self, repository):
        self.repository = repository

    def post_list(self):
        return self.repository.get_all()

    def post_create(self, post_dto: PostCreateDTO):
        return self.repository.post_create(post_dto)

    def post_detail(self, post_id: int):
        return self.repository.get_by_id(post_id)

    def post_delete(self, post_id: int) -> bool:
        return self.repository.delete_by_id(post_id)

    def post_update(self, post_id: int, post_dto):
        return self.repository.update_by_id(post_id, post_dto)

    def post_like(self, post_id: int, user):
        all_users_like = self.repository.get_by_id(post_id).like.all()
        if user not in all_users_like:
            self.repository.get_by_id(post_id).like.add(user)
            return True
        else:
            self.repository.get_by_id(post_id).like.remove(user)
            return False
