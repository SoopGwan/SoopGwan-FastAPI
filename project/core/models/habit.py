from sqlalchemy import BigInteger, Column, DATE, ForeignKey, String
from sqlalchemy.orm import relationship
from project.core.models import Base

class Habit(Base):
    __tablename__ = 'tbl_habit'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    content = Column(String(200), nullable=False)
    start_at = Column(DATE, nullable=False)
    end_at = Column(DATE, nullable=False)
    user_id = Column(ForeignKey('user.id'), index=True)
    day_id = Column(ForeignKey('day.id'), index=True)
    count = Column(BIGINT, nullable=False)

    day = relationship('Day')
    user = relationship('User')