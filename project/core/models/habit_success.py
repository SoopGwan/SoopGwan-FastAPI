from sqlalchemy import Column, BigInteger, Date, ForeignKey
from sqlalchemy.orm import relationship
from project.core.models import Base

class HabitSucces(Base):
    __tablename__ = 'tbl_habit_success'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    success_at = Column(Date, nullable=False)
    week_habit_id = Column(ForeignKey('tbl_week_habit.id'), index=True)

    week_habit = relationship('WeekHabit')