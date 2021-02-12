from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from database import database
from .player import Player
from .item import Item


class Thing(database.base):
    """
    Spawned thing that on spawn should belong to someone.
    user_id is 0 when encounter is wielding this thing.
    """
    __tablename__ = "things"

    thing_id = Column(BigInteger, primary_key=True)  # in-game specific item
    user_id = Column(BigInteger, ForeignKey(Player.user_id))  # user
    item_id = Column(BigInteger, ForeignKey(Item.item_id))  # base of item

    item = relationship('Item', foreign_keys='Thing.item_id')
