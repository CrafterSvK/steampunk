import enum

from sqlalchemy import Column, BigInteger, ForeignKey, VARCHAR
from database.db import db
from database.player import Player


class ItemType(enum.Enum):
    recipe = 1
    weapon = 2
    gear = 3
    part = 3
    herb = 4
    potion = 5
    misc = 99


class Item(db.base):
    """
    Spawned item that should belong to someone.
    user_id is 0 when encounter is wielder.
    """
    __tablename__ = "items"

    item_id = Column(BigInteger, primary_key=True, autoincrement=True)  # in-game specific item
    user_id = Column(BigInteger, ForeignKey(Player.user_id))  # user
    entity_id = Column(VARCHAR(50))  # base of item
