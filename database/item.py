from sqlalchemy import Column, BigInteger, Text, VARCHAR
from sqlalchemy.types import Enum

from database import database


class ItemType(Enum.enum):
    recipe = 1
    weapon = 2
    gear = 3
    part = 3
    herb = 4
    potion = 5
    misc = 99


class Item(database.base):
    """
    Items should be defined here. Structure is not known. WIP.
    """
    __tablename__ = "items"

    item_id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR)
    type = Column(Enum(ItemType))
    desc = Column(Text)
