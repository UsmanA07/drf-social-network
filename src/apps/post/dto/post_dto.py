from dataclasses import dataclass


@dataclass
class PostListDTO:
    id: int
    user: str
    title: str
    text: str
    published: str
