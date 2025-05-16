from dataclasses import dataclass


@dataclass
class CommentListDTO:
    id: int
    user: str
    post: str
    text: str
    published: str
