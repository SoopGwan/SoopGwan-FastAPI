from sqlalchemy import Column, ForeignKey, INT
from sqlalchemy.orm import relationship
from project.core.models import Base

class HabitSucces(Base):
    __tablename__ = 'tbl_habit_success'

    user_id = Column(ForeignKey('user.id'), primary_key=True)
    habit_id = Column(ForeignKey('habit.id'), primary_key=True, index=True)
    success = Column(INT, nullable=False)

    habit = relationship('Habit')
    user = relationship('User')