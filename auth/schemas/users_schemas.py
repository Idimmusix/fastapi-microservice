import datetime as dt

from fastapi import File, UploadFile

from pydantic import BaseModel, Field
from typing import List, Optional, Any


class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True

class User(UserBase):
    id: str
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    is_active: Optional[bool]
    has_password: Optional[bool]
    is_verified: bool
    is_superuser: bool
    org_user: Optional[List[OrgUser]]
    country_code: Optional[str]
    image_url: Optional[str] 
    is_deleted: bool
    device_id: Optional[str] 
    country: Optional[str]
    state: Optional[str]
    google_id: Optional[str]
    google_image_url: Optional[str] 
    date_created: dt.datetime
    last_updated: dt.datetime 

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    id: str
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True

class UserActivate(UserBase):
    is_active: bool

class UserResetPassword(UserBase):
    email: Optional[str]
    code: str
    password: str


class AuthToken(BaseModel):
    id: str
    user_id: str
    token: str

class OrganizationBase(BaseModel):
    id: str
    name: str
    user_id: str

    class Config:
        orm_mode = True


class RoleBase(BaseModel):
    role_name: str
    organization_id: Optional[str]
    permissions: Optional[List[str]]
    class Config:
        orm_mode = True

class UserInvitations(BaseModel):
    organization_id: str
    user_id: str
    email: str
    role_id: str
    invite_code: str
    is_accepted: str
    is_revoked: str
    organization: OrganizationBase
    # user: UserBase
    role: RoleBase

    class Config:
        orm_mode = True

class UserPasswordUpdate(BaseModel):
    code: str
    password: str

class UserTokenVerification(BaseModel):
    email: str
    redirect_url: str
    
class UserCodeVerification(BaseModel):
    email: str
    code_length: Optional[int] = Field(None, title="This is the length of the verification code, which is 6 by default", example=5)

class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserInfo(UserBase):
    first_name: str
    last_name: str


class UserOrgLogin(UserBase):
    password: str
    organization: str

    
class UserLogin(UserBase):
    password: str

class UserRecoverPassword(UserBase):
    pass

class OrgUser(BaseModel):
    id: Optional[str]
    organization_id: str
    user_id: str
    role_id: str
    user_permissions: Optional[List[str]]
    is_deleted: bool
    date_created: Optional[dt.datetime]
    last_updated: Optional[dt.datetime]
    role: Optional[RoleBase]

    class Config:
        orm_mode = True

class UserCreateOut(User):
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        orm_mode = True

class UpdateUserReq(UserBase):
    first_name: Optional[str]
    last_name: Optional[str]
    country_code: Optional[str]
    phone_number: Optional[str]
    country: Optional[str]
    state: Optional[str]
   
    class Config:
        orm_mode = True
        
        
class updatePasswordRequest(BaseModel):
    password:str
    password_confirmation:str
    

class ImageUploadReq(BaseModel):
    image: UploadFile = File(...)
    




