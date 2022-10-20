from sqlalchemy import BIGINT, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from project.core.models import Base

class Achive(Base):
    __tablename__ = 'tbl_achive'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    condition = Column(String(200), nullable=False)
    title = Column(String(10), nullable=False)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)

    user = relationship('User')