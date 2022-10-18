from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT
from project.core.models import Base

class TblHabitSucces(Base):
    __tablename__ = 'tbl_habit_success'

    user_id = Column(ForeignKey('tbl_user.id'), primary_key=True, nullable=False, server_default=text("'0'"))
    habit_id = Column(ForeignKey('tbl_habit.id'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    success = Column(TINYINT(1), nullable=False, server_default=text("'0'"))

    habit = relationship('TblHabit')
    user = relationship('TblUser')