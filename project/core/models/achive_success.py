from sqlalchemy import Column, DATETIME, BigInteger, ForeignKey

from project.core.models import Base


class Achive_Success(Base):
    __tablename__ = "achive_success"

    user_id = Column(BigInteger, ForeignKey("user.id"), primary_key=True)
    achive_id = Column(BigInteger, ForeignKey("achive.id"), primary_key=True)
    date = Column(DATETIME, nullable=False)