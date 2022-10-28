from pydantic import BaseModel, validator, constr
from fastapi import HTTPException, status

class SendCode(BaseModel):
    phone_number: constr()
    @validator('phone_number')
    def check_phone_number(cls, v):
        if len(v) != 11 or v[:3] != "010":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="전화번호 형식이 잘못됨.")
        return v

class VerifyCode(BaseModel):
    phone_number: constr(min_length=11, max_length=11)
    code: constr(min_length=4, max_length=4)

class SignUp(BaseModel):
    phone_number: constr(min_length=11, max_length=11)
    account_id: constr(min_length=6, max_length=24)
    password: constr(min_length=8, max_length=24)