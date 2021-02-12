from sqlalchemy import Column, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.types import Enum

from database import database


class SexEnum(Enum.enum):
    female = 1
    male = 2


class Player(database.base):
    """
    Player which is played by people on Discord.
    """
    __tablename__ = "players"

    user_id = Column(BigInteger, primary_key=True)
    sex = Column(Enum(SexEnum))
    level = Column(BigInteger, default=1)
    xp = Column(BigInteger, default=0)

    # Basic attributes
    strength = Column(TINYINT, default=1)
    agility = Column(TINYINT, default=1)
    resistance = Column(TINYINT, default=1)
    endurance = Column(TINYINT, default=1)
    intelligence = Column(TINYINT, default=1)
    perception = Column(TINYINT, default=1)
    luck = Column(TINYINT, default=1)

    equipment = relationship('Equipment', foreign_keys='Player.user_id')
