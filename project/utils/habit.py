from sqlalchemy.orm import Session
from project.core.models.week_habit import WeekHabit
from datetime import datetime, timedelta
from fastapi import HTTPException, status
def create_habit(content: str, user_id: str, session: Session):
    session.add(
        WeekHabit(
            content=content,
            user_id=user_id,
            start_at=datetime.now().date() - timedelta(days=datetime.today().weekday()),
            end_at=datetime.now().date() - timedelta(days=datetime.today().weekday()-6),
            status=None
        )
    )
    return {
        "message": "success"
    }

def delete_habit(habit_id: str, user_id: str, session: Session):
    habit = session.query(WeekHabit).filter(WeekHabit.id==habit_id).scalar()
    if not habit: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="해당 id가 존재하지 않음.")
    if habit.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="사용자의 습관이 아님.")
    session.delete(habit)
    return