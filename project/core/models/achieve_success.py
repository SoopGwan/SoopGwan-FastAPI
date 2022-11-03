from sqlalchemy import Column, BigInteger, Date, ForeignKey
from project.core.models import Base

class AchieveSuccess(Base):
    __tablename__ = "tbl_achieve_success"

    user_id = Column(BigInteger, ForeignKey('tbl_user.id'), index=True),
    achiveve_id = Column(BigInteger, ForeignKey('tbl_achieve.id'), index=True),
    date = Column(Date, Date, nullable=False)