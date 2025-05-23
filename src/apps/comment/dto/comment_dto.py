from dataclasses import dataclass

from apps.post.models import Post
from apps.user.models import ProfileUser


@dataclass
class CommentListDTO:
    id: int
    user: ProfileUser
    post: Post
    text: str
    published: str


@dataclass
class CommentCreateDTO:
    user: ProfileUser
    post: int
    text: str


@dataclass
class CommentDeleteDTO:
    id: int
    user: ProfileUser
    post: Post
    text: str
    published: str


@dataclass
class CommentUpdateDTO:
    text: str
    user: ProfileUser

@dataclass
class CommentDetailDTO:
    id: int
    user: ProfileUser
    post: Post
    text: str
    published: str