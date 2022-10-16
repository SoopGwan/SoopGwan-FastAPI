from sqlalchemy import Column, VARCHAR, CHAR, BigInteger
from sqlalchemy.orm import relationship

from project.core.models import Base
from project.core.models.achive import Achive
from project.core.models.achive_success import Achive_Success
from project.core.models.habit import Habit
from project.core.models.habit_success import Habit_Success


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    account_id = Column(VARCHAR(24), nullable=False)
    password = Column(CHAR(60), nullable=False)
    name = Column(VARCHAR(10), nullable=False)
    phone_number = Column(VARCHAR(11), nullable=False)
    level = Column(CHAR(3), nullable=False)

    achive = relationship(Achive, backref="user")
    achive_success = relationship(Achive_Success, backref="user")
    habit = relationship(Habit, backref="user")
    habit_success = relationship(Habit_Success, backref="user")