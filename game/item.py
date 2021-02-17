from sqlalchemy.sql.expression import select

import database as db
from database.db import session
from entities import weapons


class Item:
    def __init__(self, item_id: int):
        self.item_id = item_id
        self.name = "empty"

        if item_id is not None:
            item = session.execute(
                select(db.Item).filter_by(item_id=self.item_id)
            ).scalar_one()

            self.entity_id = item.entity_id
            self.name = weapons[item.entity_id]['name']
            self.desc = weapons[item.entity_id]['desc']
