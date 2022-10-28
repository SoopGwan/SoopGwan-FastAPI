from pydantic import BaseModel, validator, constr
from fastapi import HTTPException, status
import re

class SendCode(BaseModel):
    phone_number: constr()
    @validator('phone_number')
    def check_phone_number(cls, v):
        if len(v) != 11 or v[:3] != "010":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="전화번호 형식이 잘못됨.")
        return v

class VerifyCode(BaseModel):
    phone_number: constr()
    code: constr()

    @validator('phone_number')
    def check_phone_number(cls, v):
        if len(v) != 11 or v[:3] != "010":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="전화번호 형식이 잘못됨.")
        return v

    @validator('code')
    def check_code(cls, v):
        if len(v) != 4:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="인증코드 형식이 잘못됨.")
        return v

class SignUp(BaseModel):
    phone_number: constr()
    account_id: constr()
    password: constr()

    @validator('phone_number')
    def check_phone_number(cls, v):
        if len(v) != 11 or v[:3] != "010":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="전화번호 형식이 잘못됨.")
        return v

    @validator('account_id')
    def check_account_id(cls, v):
        if len(v) != 11 or v[:3] != "010":
            REGEX_ID = r'^[A-Za-z0-9]{6,24}$'
            if not re.fullmatch(REGEX_ID, v):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="아이디 형식이 잘못됨.")
        return v

    @validator('password')
    def check_password(cls, v):
        REGEX_PASSWORD = r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,}$'
        if not re.fullmatch(REGEX_PASSWORD, v):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호 형식이 잘못됨")
        return v

def Login(BaseModel):
    account_id: constr()
    password: constr()

    @validator('account_id')
    def check_account_id(cls, v):
        if len(v) != 11 or v[:3] != "010":
            REGEX_ID = r'^[A-Za-z0-9]{6,24}$'
            if not re.fullmatch(REGEX_ID, v):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="아이디 형식이 잘못됨.")
        return v

    @validator('password')
    def check_password(cls, v):
        REGEX_PASSWORD = r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,}$'
        if not re.fullmatch(REGEX_PASSWORD, v):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="비밀번호 형식이 잘못됨")
        return v