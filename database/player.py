import enum

from sqlalchemy import Column, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.types import Enum
from sqlalchemy.sql import func

from database import database
from database.equipment import Equipment


class SexEnum(enum.Enum):
    female = 1
    male = 2


class Player(database.base):
    """
    Player which is played by people on Discord.
    """
    __tablename__ = "players"

    user_id = Column(BigInteger, ForeignKey(Equipment.user_id), primary_key=True, autoincrement=False)
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

    # Skills
    cold_weapons = Column(TINYINT, default=0)
    steam_weapons = Column(TINYINT, default=0)
    metallurgy = Column(TINYINT, default=0)
    crafting = Column(TINYINT, default=0)
    herbalism = Column(TINYINT, default=0)
    potion_making = Column(TINYINT, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    equipment = relationship('Equipment', foreign_keys='Player.user_id')
