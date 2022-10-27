from sqlalchemy import Column, BigInteger, String, CHAR
from project.core.models import Base

class User(Base):
    __tablename__ = "tbl_user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    account_id = Column(String(24), nullable=False)
    password = Column(CHAR(60), nullable=False)
    name = Column(String(10), nullable=False)
    phone_number = Column(CHAR(11), nullable=False)