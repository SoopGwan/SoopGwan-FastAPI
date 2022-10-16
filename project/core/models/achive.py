from sqlalchemy import Column, VARCHAR, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from project.core.models import Base
from project.core.models.achive_success import Achive_Success


class Achive(Base):
    __tablename__ = "achive"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    condition = Column(VARCHAR(200), nullable=False)
    title = Column(VARCHAR(10), nullable=False)
    user_id = Column(BigInteger, ForeignKey("user.id"), primary_key=True)

    comment = relationship(Achive_Success, backref="achive")