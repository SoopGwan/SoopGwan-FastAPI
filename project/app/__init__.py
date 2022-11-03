from fastapi import APIRouter

from project.app import user, habit

api_router = APIRouter()

api_router.include_router(user.user_router, prefix="/users", tags=["user"])
api_router.include_router(habit.habit_router, prefix="/habits", tags=["habit"])