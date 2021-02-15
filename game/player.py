import discord

from database import session
from database.player import Player as Character
from database.item import Item as DBItem

from game.item import Item


class Player:
    def __init__(self, user: discord.Member):
        self.user = user

        character = session.query(Character).filter(Character.user_id == self.user.id).one_or_none()

        if character is None:
            player = Character()
            player.id = self.user.id

            session.add(player)
            session.commit()

    def get_inventory_contents(self):
        contents = session.query(DBItem).filter(DBItem.user_id == self.user.id).all()

        return [Item(item.entity_id) for item in contents]
