from dataclasses import dataclass


@dataclass
class UserRegisterDTO:
    username: str
    first_name: str
    last_name: str
    phone: str
    email: str
    password: str
