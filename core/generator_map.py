from core.terrains.field import Field
from core.terrains.forest import Forest
from core.terrains.graveyard import Graveyard
import random


def generate_map():

    # TODO auto added
    field = Field()
    forest = Forest()
    graveyard = Graveyard()

    weighted_choices = [
        (field.emoji_icon, field._rarity),
        (forest.emoji_icon, forest._rarity),
        (graveyard.emoji_icon, graveyard._rarity),
    ]
    terrains = [val for val, cnt in weighted_choices for i in range(cnt)]

    rows = []
    for i in range(7):
        cols = []
        for j in range(7):
            cols.append(random.choice(terrains))
        rows.append(cols)

    return rows