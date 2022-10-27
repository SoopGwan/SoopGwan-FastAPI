from pydantic import BaseModel, constr

class SendCode(BaseModel):
    phone_number: constr(min_length=11, max_length=11)

class VerifyCode(BaseModel):
    phone_number: constr(min_length=11, max_length=11)
    code: constr(min_length=4, max_length=4)