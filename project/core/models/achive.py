from sqlalchemy import BigInteger, Column, ForeignKey, String, text
from sqlalchemy.orm import relationship
from project.core.models import Base

class TblAchive(Base):
    __tablename__ = 'tbl_achive'

    id = Column(BigInteger, primary_key=True, server_default=text("'0'"))
    condition = Column(String(200), nullable=False)
    title = Column(String(10), nullable=False)
    user_id = Column(ForeignKey('tbl_user.id'), nullable=False, index=True, server_default=text("'0'"))

    user = relationship('TblUser')