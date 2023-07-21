from .base import BaseTerrain


class Field(BaseTerrain):

    _title = 'Поле'
    _emoji_icon = '🌿'
    _transit_time = 3
    _rarity = 8
    _seed_list = [
        'Цветочное',
        'Пшеничное',
        'Травянистое',
    ]
