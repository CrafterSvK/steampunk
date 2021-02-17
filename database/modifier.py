from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.dialects.mysql.types import SMALLINT
from sqlalchemy.orm import relationship

from database.db import db
from database.item import Item


class Modifier(db.base):
    """
    Modifier for "things"
    """
    __tablename__ = "modifiers"

    modifier_id = Column(BigInteger, autoincrement=True, primary_key=True)
    item_id = Column(BigInteger, ForeignKey(Item.item_id))

    # Basic attributes
    strength = Column(SMALLINT, default=0)
    agility = Column(SMALLINT, default=0)
    resistance = Column(SMALLINT, default=0)
    endurance = Column(SMALLINT, default=0)
    intelligence = Column(SMALLINT, default=0)
    perception = Column(SMALLINT, default=0)
    luck = Column(SMALLINT, default=0)

    cold_weapons = Column(SMALLINT, default=0)
    steam_weapons = Column(SMALLINT, default=0)
    metallurgy = Column(SMALLINT, default=0)
    crafting = Column(SMALLINT, default=0)
    herbalism = Column(SMALLINT, default=0)
    potion_making = Column(SMALLINT, default=0)

    item = relationship('Item', foreign_keys='Modifier.item_id')
