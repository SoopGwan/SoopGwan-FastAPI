from pydantic import BaseModel, constr, validator
from fastapi import HTTPException, status

class CreateHabit(BaseModel):
    content: constr()
    @validator('content')
    def check_content(cls, v):
        if not v or len(v) > 200: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Content가 잘못됨.")
        return v