from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, text
from sqlalchemy.orm import relationship
from project.core.models import Base

class TblHabit(Base):
    __tablename__ = 'tbl_habit'

    id = Column(BigInteger, primary_key=True, server_default=text("'0'"))
    content = Column(String(200), nullable=False)
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    user_id = Column(ForeignKey('tbl_user.id'), nullable=False, index=True, server_default=text("'0'"))
    day_id = Column(ForeignKey('tbl_day.id'), nullable=False, index=True, server_default=text("'0'"))
    count = Column(BigInteger, nullable=False, server_default=text("'0'"))

    day = relationship('TblDay')
    user = relationship('TblUser')