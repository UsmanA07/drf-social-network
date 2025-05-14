from dataclasses import dataclass


@dataclass
class UserRegisterDTO:
    username: str
    first_name: str | None
    last_name: str | None
    phone: str | None
    email: str
    password: str
