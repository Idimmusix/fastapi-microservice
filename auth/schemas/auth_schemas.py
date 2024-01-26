import datetime as dt
from typing import Optional
from enum import Enum
from pydantic import BaseModel, root_validator, EmailStr

from timbuapi.core.exceptions import EmptyStringException
from timbuapi.utils.utils import is_empty_string


class AccessLevel(str, Enum):
    full_access = "full_access"
    read_only = "read_only"
    write_only = "write_only"

    
class _UserBase(BaseModel):
    email: Optional[str]


class UserUpdate(_UserBase):
    first_name: str
    last_name: str


class UserPasswordUpdate(BaseModel):
    password: str


class TestIn(_UserBase):
    username: str
    password: str
    full_name: str


class TestOut(_UserBase):
    username: str
    full_name: str


class UserCreate(_UserBase):
    email: EmailStr
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    phone_country_code: Optional[str]
    image_url: Optional[str]
    device_id: Optional[str]
    # country: Optional[str]
    # state: Optional[str]
    google_id: Optional[str]
    google_image_url: Optional[str]

    class Config:
        orm_mode = True

    @root_validator
    def validate_empty_string(cls, values):
        email = values.get('email')
        password = values.get('password')
        first_name = values.get('first_name')
        last_name = values.get('last_name')

        if email is not None and is_empty_string(email):
            raise EmptyStringException('email cannot be empty')
        if password is not None and is_empty_string(password):
            raise EmptyStringException('password cannot be empty')
        if first_name is not None and is_empty_string(first_name):
            raise EmptyStringException('first_name cannot be empty')
        if last_name is not None and is_empty_string(last_name):
            raise EmptyStringException('last_name cannot be empty')

        return values
        

class UserCreateSync(BaseModel):
    id: Optional[str]
    password: str
    email: str
    organization_id: str
    role_id: str
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    phone_country_code: Optional[str]
    image_url: Optional[str]
    device_id: Optional[str]
    google_id: Optional[str]
    google_image_url: Optional[str]

    class Config:
        orm_mode = True


class UserCreateOut(_UserBase):
    id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    is_deleted: Optional[bool]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]
    has_password: Optional[bool]
    phone_number: Optional[str]
    phone_country_code: Optional[str]
    image_url: Optional[str]
    device_id: Optional[str]
    google_id: Optional[str]
    google_image_url: Optional[str]

    class Config:
        orm_mode = True

class CustomerPassword(BaseModel):
    password: str
    
    class Config:
        orm_mode = True

class CustomerLogin(BaseModel):
    email: str
    password: Optional[str]
    organization_id: str
    app_url: Optional[str]

    class Config:
        orm_mode = True


class CustomerAuthOut(BaseModel):
    biz_partner_id: Optional[str]
    first_name: str
    last_name: str
    organization_id: str

    class Config:
        orm_mode = True


class UserLogin(_UserBase):
    phone_number: Optional[str]
    phone_country_code: Optional[str]
    device_id: Optional[str]
    password: str


class MagicLogin(BaseModel):
    token: str
    organization_id: str
    redirect_url: Optional[str]



class Token(_UserBase):
    access_token: str
    token_type: str


class TokenData(_UserBase):
    id: Optional[str] = None
    type: Optional[str]

class Logout(BaseModel):
    user_id: str

class User(_UserBase):
    id: str
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    is_active: bool
    is_verified: bool
    is_superuser: bool
    phone_country_code: Optional[str]
    image_url: Optional[str]
    is_deleted: bool
    device_id: Optional[str]
    google_id: Optional[str]
    google_image_url: Optional[str]
    date_created: dt.datetime
    last_updated: dt.datetime

    class Config:
        orm_mode = True


class APIKey(_UserBase):
    app_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    phone_country_code: Optional[str]
    user_id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    access_level: Optional[AccessLevel] = "full_access"


class APIKEYCheck(BaseModel):
    app_id: str
    api_key: str

class ApiKeyAuth(BaseModel):
    APP_ID: str
    API_KEY: str

class SUAuth(BaseModel):
    email: str
    password: str

class APIKeyReset(_UserBase):
    code: str
