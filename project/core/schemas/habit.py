from fastapi import HTTPException, status
from pydantic import BaseModel, constr, validator


class CreateHabit(BaseModel):
    content: constr()
    @validator('content')
    def check_content(cls, v):
        if not v or len(v) > 200: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Content가 잘못됨.")
        return v

class DeleteHabit(BaseModel):
    id: constr()
    @validator('id')
    def check_id(cls, v):
        if not v or not v.isdigit(): raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="habit가 잘못됨.")
        return v