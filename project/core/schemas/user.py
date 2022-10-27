from pydantic import BaseModel, constr

class SendCode(BaseModel):
    phone_number: constr(min_length=11, max_length=11)