from project.core import session_scope

from fastapi import APIRouter, status, Depends, Response
from project.utils.user import get_current_user
from project.core.models.user import User
from project.core.schemas.habit import CreateHabit, DeleteHabit
from project.utils.habit import create_habit, delete_habit

habit_router = APIRouter()


@habit_router.post("/")
async def creating_habit(request: CreateHabit, user: User = Depends(get_current_user)):
    with session_scope() as session:
        create_habit(content=request.content, user_id=user.id, session=session)
        return Response(status_code=201)


@habit_router.delete("/")
async def deleting_habit(request: DeleteHabit, user: User = Depends(get_current_user)):
    with session_scope() as session:
        delete_habit(habit_id=request.id, user_id=user.id, session=session)
        return Response(status_code=204)