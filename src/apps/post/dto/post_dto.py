from dataclasses import dataclass


@dataclass
class PostListDTO:
    id: int
    user: str
    title: str
    text: str
    published: str


@dataclass
class PostCreateDTO:
    title: str
    text: str
    user: str


@dataclass
class PostDetailDTO:
    id: int
    user: str
    title: str
    text: str
    published: str


@dataclass
class PostUpdateDTO:
    title: str | None
    text: str | None
