from .base import BaseTerrain


class Forest(BaseTerrain):

    _title = 'Лес'
    _emoji_icon = '🌳'
    _transit_time = 3
    _rarity = 8
    _seed_list = [
        'Березовый',
        'Хвойный',
        'Смешанный',
    ]
