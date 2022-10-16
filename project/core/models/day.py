from sqlalchemy import Column, DATETIME, BigInteger

from project.core.models import Base

class Day(Base):
    __tablename__ = "day"

    start_at = Column(DATETIME, nullable=False)
    end_at = Column(DATETIME, nullable=False)
    eval = Column(BigInteger, nullable=False)