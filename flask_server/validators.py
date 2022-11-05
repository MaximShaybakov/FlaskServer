import re
import bcrypt
import pydantic
from typing import Type, Optional
from flask_bcrypt import Bcrypt
from main import app



bcrypt = Bcrypt(app)


class CreateUserShema(pydantic.BaseModel):

    def __init__(self):
        self.password_regex = re.compile(r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=*_!-]).*$')
        self.email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    name: str
    password: str
    email: str

    @pydantic.validator('name')
    def check_name(cls, value: str):
        if len(value) < 2:
            raise ValueError('name mast be less then 2 chars')
        return value

    @pydantic.validator('password')
    def check_password(cls, value: str):
        if not re.search(self.password_regex, value):
            raise ValueError('password is to easy')
        value = value.encode()
        value = bcrypt.generate_password_hash(value)
        value = value.decode()
        return value

    @pydantic.validator('email')
    def check_mail(cls, value: str):
        if not re.search(self.email_regex, value):
            raise ValueError('invalid email')


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
    title: Optional[str]
    content: Optional[str]


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

class PatchAdsShema(pydantic.BaseModel):

    title: Optional[str]
    content: Optional[str]

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


def validate(data_to_validate: dict, validation_class: Type[CreateAdsShema] | Type[PatchAdsShema]):
    try:
        return validation_class(**data_to_validate).dict(exclude_none=True)
    except pydantic.ValidationError as err:
        raise HttpError(400, err.errors())
