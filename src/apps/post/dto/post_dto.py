from dataclasses import dataclass

from apps.user.models import ProfileUser


@dataclass
class PostListDTO:
    id: int
    user: ProfileUser
    title: str
    text: str
    published: str


@dataclass
class PostCreateDTO:
    title: str
    text: str
    user: ProfileUser


@dataclass
class PostDetailDTO:
    id: int
    user: ProfileUser
    title: str
    text: str
    published: str
    posts_comment: list
    like_count: int
    like: list
    views_count: int


@dataclass
class PostUpdateDTO:
    title: str | None
    text: str | None
    user: ProfileUser
