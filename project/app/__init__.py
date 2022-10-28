from fastapi import APIRouter

from project.app import user

api_router = APIRouter()

api_router.include_router(user.user_router, prefix="/users", tags=["user"])