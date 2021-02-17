import discord
import database as db

from sqlalchemy.sql.expression import select, update
from database.db import session
from game.item import Item


class Player:
    def __init__(self, user: discord.Member):
        self.user = user

        character = session.query(db.Player)\
            .filter(db.Player.user_id == self.user.id)\
            .one_or_none()

        self.sex = character.sex
        self.level = character.level
        self.xp = character.xp
        self.strength = character.strength
        self.agility = character.agility
        self.resistance = character.resistance
        self.endurance = character.endurance
        self.intelligence = character.intelligence
        self.perception = character.perception
        self.luck = character.luck

        if character is None:
            player = db.Player()
            player.user_id = self.user.id
            player.sex = "male"

            equipment = db.Player()
            equipment.user_id = self.user.id

            session.add(player)
            session.commit()

    def get_inventory_contents(self):
        contents = session.execute(
            select(db.Item).filter_by(user_id=self.user.id)
        ).scalars().all()

        return [Item(item.item_id) for item in contents]
    
    def get_equipment(self) -> dict[str, Item]:
        equipment = session.execute(
            select(db.Equipment).filter_by(user_id=self.user.id)
        ).scalar_one()

        return {
            "head": Item(equipment.head),
            "body": Item(equipment.body),
            "left_hand": Item(equipment.left_hand),
            "right_hand": Item(equipment.right_hand),
            "legs": Item(equipment.legs),
            "foot": Item(equipment.foot)
        }

    def equip(self, item: Item) -> bool:
        equipped = session.execute(
            update(db.Equipment).where(db.Equipment.user_id == self.user.id).
            values(right_hand=item.item_id)
        )

        return equipped

    def get_attributes(self) -> dict[str, int]:
        return {
            "Sex": self.sex,
            "Level": self.level,
            "XP": self.xp,
            "Strength": self.strength,
            "Agility": self.agility,
            "Resistance": self.resistance,
            "Endurance": self.endurance,
            "Intelligence": self.intelligence,
            "Perception": self.perception,
            "Luck": self.luck
        }

    def get_skills(self) -> dict[str, int]:
        return {
            "Herbalism": 0
        }
