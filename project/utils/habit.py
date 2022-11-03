from sqlalchemy.orm import Session
from project.core.models.week_habit import WeekHabit
from datetime import datetime, timedelta
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