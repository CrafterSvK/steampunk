from sqlalchemy import Column, BigInteger, ForeignKey, VARCHAR
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.orm import relationship
from database.db import db
from database.player import Player


class Encounter(db.base):
    """
    Spawned living-entity with additional/copied characteristics.
    Same rules apply for Entities as for Players.
    They can wield gear and use weaponry.
    """
    __tablename__ = "encounters"

    encounter_id = Column(BigInteger, autoincrement=True, primary_key=True)
    entity_id = Column(VARCHAR(50))
    user_id = Column(BigInteger, ForeignKey(Player.user_id))

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

    player = relationship('Player', foreign_keys='Encounter.user_id')
