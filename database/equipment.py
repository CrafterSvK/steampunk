from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from database import database


class Equipment(database.base):
    """
    Equipment should probably be merged with Player. Who knows?
    """
    __tablename__ = "equipment"

    user_id = Column(BigInteger, primary_key=True)
    head = Column(BigInteger, default=0)
    body = Column(BigInteger, default=0)
    legs = Column(BigInteger, default=0)
    foot = Column(BigInteger, default=0)
    left_hand = Column(BigInteger, default=0)
    right_hand = Column(BigInteger, default=0)
