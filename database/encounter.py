from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.orm import relationship
from database import database

from entity import Entity


class Encounters(database.base):
    """
    Spawned entity with additional characteristics. Same rules applies for Players too.
    They can wield gear and use weaponry.
    """
    __tablename__ = "encounters"

    encounter_id = Column(BigInteger, autoincrement=True, primary_key=True)
    entity_id = Column(BigInteger, ForeignKey(Entity.entity_id))

    # Basic attributes
    strength = Column(TINYINT, default=1)
    agility = Column(TINYINT, default=1)
    resistance = Column(TINYINT, default=1)
    endurance = Column(TINYINT, default=1)
    intelligence = Column(TINYINT, default=1)
    perception = Column(TINYINT, default=1)
    luck = Column(TINYINT, default=1)

    # Equipment
    head = Column(BigInteger, default=0)
    body = Column(BigInteger, default=0)
    legs = Column(BigInteger, default=0)
    foot = Column(BigInteger, default=0)
    left_hand = Column(BigInteger, default=0)
    right_hand = Column(BigInteger, default=0)

    entity = relationship('Entity', foreign_keys='Encounter.entity_id')
