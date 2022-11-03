from sqlalchemy import Column, BigInteger, String, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship
from project.core.models import Base

class WeekHabit(Base):
    __tablename__ = 'tbl_week_habit'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    content = Column(String(200), nullable=False)
    start_at = Column(Date, nullable=False)
    end_at = Column(Date, nullable=False)
    status = Column(Integer, nullable=False)
    user_id = Column(ForeignKey('tbl_user.id'), index=True)

    user = relationship('User')