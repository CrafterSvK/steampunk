from sqlalchemy import Column, BigInteger, VARCHAR
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.orm import relationship

from database import database


class Entity(database.base):
    """
    Basic entity, everything you can touch, fight with and can react to your actions.
    Entity isn't spawned. When spawned it transforms to encounter.
    """
    __tablename__ = "entities"

    entity_id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR, not_null=True)
    strength = Column(TINYINT, default=1)
    agility = Column(TINYINT, default=1)
    resistance = Column(TINYINT, default=1)
    endurance = Column(TINYINT, default=1)
    intelligence = Column(TINYINT, default=1)
    perception = Column(TINYINT, default=1)
    luck = Column(TINYINT, default=1)

    entity = relationship('Entity', foreign_keys='Encounter.entity_id')
