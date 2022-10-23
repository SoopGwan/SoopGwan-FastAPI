from sqlalchemy import Column, DATE, ForeignKey
from sqlalchemy.orm import relationship
from project.core.models import Base

class AchiveSucces(Base):
    __tablename__ = 'tbl_achive_success'

    user_id = Column(ForeignKey('user.id'), primary_key=True)
    achive_id = Column(ForeignKey('achive.id'), primary_key=True, index=True)
    date = Column(DATE, nullable=False)

    achive = relationship('Achive')
    user = relationship('User')