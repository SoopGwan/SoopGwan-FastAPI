from sqlalchemy import BigInteger, Column, DATE
from project.core.models import Base


class Day(Base):
    __tablename__ = 'tbl_day'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    start_at = Column(DATE, nullable=False)
    end_at = Column(DATE, nullable=False)
    eval = Column(BigInteger, nullable=False)