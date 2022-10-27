from pydantic import BaseModel, constr

class SendCode(BaseModel):
    phone_number: constr(min_length=11, max_length=11)

class VerifyCode(BaseModel):
    phone_number: constr(min_length=11, max_length=11)
    code: constr(min_length=4, max_length=4)

class SignUp(BaseModel):
    phone_number: constr(min_length=11, max_length=11)
    account_id: constr(min_length=6, max_length=24)
    password: constr(min_length=8, max_length=24)