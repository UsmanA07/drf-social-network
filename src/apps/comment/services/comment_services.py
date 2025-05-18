from apps.comment.dto.comment_dto import CommentCreateDTO, CommentUpdateDTO


class CommentServices:
    def __init__(self, repository):
        self.repository = repository

    def comment_list(self, post_id: int):
        return self.repository.get_all(post_id)

    def comment_create(self, comment_dto: CommentCreateDTO, post_id: int) -> CommentCreateDTO:
        return self.repository.comment_create(comment_dto, post_id)

    def comment_delete(self, comment_id: int):
        return self.repository.delete_by_id(comment_id)

    def comment_update(self, comment_id: int, comment_dto: CommentUpdateDTO) -> CommentUpdateDTO:
        print(comment_dto, 'ser')
        return self.repository.update_by_id(comment_id, comment_dto)
