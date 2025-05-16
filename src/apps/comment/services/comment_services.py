class CommentServices:
    def __init__(self, repository):
        self.repository = repository

    def comment_list(self, post_id):
        return self.repository.get_all(post_id)
