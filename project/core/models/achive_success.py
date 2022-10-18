from sqlalchemy import Column, DateTime, ForeignKey, text
from sqlalchemy.orm import relationship
from project.core.models import Base

class TblAchiveSucces(Base):
    __tablename__ = 'tbl_achive_success'

    user_id = Column(ForeignKey('tbl_user.id'), primary_key=True, nullable=False, server_default=text("'0'"))
    achive_id = Column(ForeignKey('tbl_achive.id'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    date = Column(DateTime, nullable=False)

    achive = relationship('TblAchive')
    user = relationship('TblUser')