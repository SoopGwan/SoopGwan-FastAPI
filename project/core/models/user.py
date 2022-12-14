from sqlalchemy import Column, BigInteger, String
from project.core.models import Base

class User(Base):
    __tablename__ = "tbl_user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    account_id = Column(String(24), nullable=False)
    password = Column(String(60), nullable=False)
    phone_number = Column(String(11), nullable=False)