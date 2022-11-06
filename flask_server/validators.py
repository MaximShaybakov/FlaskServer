import pydantic
from typing import Type, Optional
import re
from gen_variables import bcrypt


password_regex = re.compile(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=*_!-]).*$')
email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


class CreateUserShema(pydantic.BaseModel):

    name: str
    password: str
    email: Optional[str]

    @pydantic.validator('name')
    def check_name(cls, value: str):
        if len(value) < 2:
            raise ValueError('name mast be less then 2 chars')
        return value

    @pydantic.validator('password')
    def check_password(cls, value: str):
        if not re.search(password_regex, value):
            raise ValueError('password is to easy')
        value = value.encode()
        value = bcrypt.generate_password_hash(value)
        value = value.decode()
        return value

    @pydantic.validator('email')
    def check_mail(cls, value: str):
        if not re.search(email_regex, value):
            raise ValueError('invalid email')
        return value


class PatchUserShema(pydantic.BaseModel):

    name: Optional[str]
    password: Optional[str]

    @pydantic.validator('name')
    def check_name(cls, value: str):
        if len(value) > 50:
            raise ValueError('name mast be less then 32 chars')
        return value

    @pydantic.validator('password')
    def check_password(cls, value: str):
        if not re.search(password_regex, value):
            raise ValueError('password is to easy')
        value = value.encode()
        value = bcrypt.generate_password_hash(value)
        value = value.decode()
        return value


def validate(data_to_validate: dict, validation_class: Type[CreateUserShema] | Type[PatchUserShema]):
    try:
        return validation_class(**data_to_validate).dict(exclude_none=True)
    except pydantic.ValidationError as err:
        raise HttpError(400, err.errors())


class CreateAdsShema(pydantic.BaseModel):
    title: str
    content: str
    user_id: int

    @pydantic.validator('title')
    def check_title(cls, value: str):
        if len(value) < 10:
            raise ValueError('ad text is too short')
        return value

    @pydantic.validator('content')
    def check_content(cls, value: str):
        if len(value) < 10:
            raise ValueError('ad content is too short')
        return value

    @pydantic.validator('user_id')
    def check_user_id(cls, value: int):
        if not isinstance(value, int):
            raise ValueError('integer only')
        return value


class PatchAdsShema(pydantic.BaseModel):

    title: Optional[str]
    content: Optional[str]
    user_id: Optional[int]

    @pydantic.validator('title')
    def check_name(cls, value: str):
        if len(value) > 50:
            raise ValueError('name mast be less then 32 chars')
        return value

    @pydantic.validator('content')
    def check_content(cls, value: str):
        if len(value) < 10:
            raise ValueError('ad content is too short')
        return value

    @pydantic.validator('user_id')
    def check_user_id(cls, value: int):
        if not isinstance(value, int):
            raise ValueError('integer only')
        return value


def validate_ads(data_to_validate: dict, validation_class: Type[CreateAdsShema] | Type[PatchAdsShema]):
    try:
        return validation_class(**data_to_validate).dict(exclude_none=True)
    except pydantic.ValidationError as err:
        raise HttpError(400, err.errors())
