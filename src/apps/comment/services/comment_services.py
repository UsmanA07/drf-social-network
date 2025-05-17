from apps.comment.dto.comment_dto import CommentCreateDTO


class CommentServices:
    def __init__(self, repository):
        self.repository = repository

    def comment_list(self, post_id):
        return self.repository.get_all(post_id)

    def comment_create(self, comment_dto: CommentCreateDTO, post_id: int) -> CommentCreateDTO:
        return self.repository.comment_create(comment_dto, post_id)
