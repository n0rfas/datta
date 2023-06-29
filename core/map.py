import random

from core.constants import CARS_SIZE
from core.terrains.field import Field
from core.terrains.forest import Forest
from core.terrains.graveyard import Graveyard
from core.terrains.village import Village


def generate_map():

    # TODO auto added
    field = Field()
    forest = Forest()
    graveyard = Graveyard()

    weighted_choices = [
        (field, field._rarity),
        (forest, forest._rarity),
        (graveyard, graveyard._rarity),
    ]
    terrains = [val for val, cnt in weighted_choices for i in range(cnt)]

    rows = []
    for i in range(CARS_SIZE):
        cols = []
        for j in range(CARS_SIZE):
            cols.append(random.choice(terrains))
        rows.append(cols)

    x = random.randint(0, CARS_SIZE - 1)
    y = random.randint(0, CARS_SIZE - 1)
    rows[x][y] = Village()

    return rows, [x, y]


def preview_map(map_):
    rows = ""
    for x in range(0, len(map_)):
        cols = ""
        for y in range(0, len(map_)):
            cols += map_[x][y].emoji_icon
        rows += cols + '\n'

    return rows
