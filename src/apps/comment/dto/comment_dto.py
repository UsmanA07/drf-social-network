from dataclasses import dataclass

from apps.post.models import Post
from apps.user.models import ProfileUser


@dataclass
class CommentListDTO:
    id: int
    user: ProfileUser
    post: str
    text: str
    published: str


@dataclass
class CommentCreateDTO:
    user: ProfileUser
    post: Post
    text: str
