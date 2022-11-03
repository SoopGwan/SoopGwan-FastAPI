from sqlalchemy import Column, BigInteger, String
from project.core.models import Base

class Achieve(Base):
    __tablename__ = 'tbl_achieve'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    unlock_condition = Column(String(200), nullable=False)
    title = Column(String(10), nullable=False)