from sqlalchemy import Column, VARCHAR, BigInteger, ForeignKey, DATETIME
from sqlalchemy.orm import relationship

from project.core.models import Base
from project.core.models.habit_success import Habit_Success
from project.core.models.day import Day

class Habit(Base):
    __tablename__ = "habit"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    context = Column(VARCHAR(200), nullable=False)
    start_at = Column(DATETIME, nullable=False)
    end_at = Column(DATETIME, nullable=False)
    count = Column(BigInteger, nullable=False)
    user_id = Column(BigInteger, ForeignKey("user.id"), primary_key=True)
    day_id = Column(BigInteger, ForeignKey("day.id"), primary_key=True)

    habit_success = relationship(Habit_Success, backref="habit")
    day = relationship(Day, backref="day")