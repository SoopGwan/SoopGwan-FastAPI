from project.core import session_scope

from fastapi import APIRouter, status, Depends
from project.utils.user import get_current_user
from project.core.models.user import User
from project.core.schemas.habit import CreateHabit
from project.utils.habit import create_habit

habit_router = APIRouter()

@habit_router.post("/", status_code=status.HTTP_201_CREATED)
async def creating_habit(response: CreateHabit, user: User = Depends(get_current_user)):
    with session_scope() as session:
        create_habit(content=response.content, user_id=user.id, session=session)
        return {
            "message": "success"
        }