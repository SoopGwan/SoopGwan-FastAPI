from sqlalchemy import Column, BigInteger, ForeignKey, BOOLEAN

from project.core.models import Base


class Habit_Success(Base):
    __tablename__ = "habit_success"

    user_id = Column(BigInteger, ForeignKey("user.id"), primary_key=True)
    habit_id = Column(BigInteger, ForeignKey("habit.id"), primary_key=True)
    success = Column(BOOLEAN, nullable=False)