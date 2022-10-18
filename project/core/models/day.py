from sqlalchemy import BigInteger, Column, DateTime, text
from project.core.models import Base


class TblDay(Base):
    __tablename__ = 'tbl_day'

    id = Column(BigInteger, primary_key=True, server_default=text("'0'"))
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    eval = Column(BigInteger, nullable=False)