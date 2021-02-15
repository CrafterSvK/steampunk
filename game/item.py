from entities import weapons


class Item:
    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.name = weapons[entity_id]['name']
