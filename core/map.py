import random

from core.constants import CARS_SIZE
from core.terrains.field import Field
from core.terrains.forest import Forest
from core.terrains.graveyard import Graveyard
from core.terrains.village import Village


def generate_map():

    # TODO auto added
    weighted_choices = [
        (Field, Field.rarity()),
        (Forest, Forest.rarity()),
        (Graveyard, Graveyard.rarity()),
    ]
    terrains = [val for val, cnt in weighted_choices for i in range(cnt)]

    rows = []
    for i in range(CARS_SIZE):
        cols = []
        for j in range(CARS_SIZE):
            T = random.choice(terrains)
            cols.append(T())
        rows.append(cols)

    y = random.randint(0, CARS_SIZE - 1)
    x = random.randint(0, CARS_SIZE - 1)
    village = Village()
    village.was_visited = True
    rows[y][x] = village

    rows[0][0].was_visited = True

    return rows, [y, x]


def preview_map(map_, hero_position):
    rows = ""
    for x in range(0, len(map_)):
        cols = ""
        for y in range(0, len(map_)):
            if hero_position == [x, y]:
                p = '🤺'
            else:
                p = map_[x][y].emoji_icon
            cols += p
        rows += cols + '\n'

    return rows
