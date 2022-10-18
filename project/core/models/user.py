from sqlalchemy import BigInteger, CHAR, Column, String, text
from project.core.models import Base

class TblUser(Base):
    __tablename__ = 'tbl_user'

    id = Column(BigInteger, primary_key=True, server_default=text("'0'"))
    account_id = Column(String(24), nullable=False)
    password = Column(CHAR(60), nullable=False)
    name = Column(String(10), nullable=False)
    phone_number = Column(CHAR(11), nullable=False)
    level = Column(CHAR(3), nullable=False)