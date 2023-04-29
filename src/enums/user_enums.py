from enum import Enum
from src.base_classes.pyenum import PyEnum


class Genders(Enum):
    female = "female"
    male = "male"


class Statuses(PyEnum):
    """
    Вариант хранения всех возможных статусов пользователя.
    Example of status enums.
    """
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    MERGED = "MERGED"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
