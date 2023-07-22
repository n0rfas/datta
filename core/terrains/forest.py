from .base import BaseTerrain


class Forest(BaseTerrain):

    _title = 'лес'
    _emoji_icon = '🌳'
    _transit_time = 3
    _rarity = 8
    _seed_list = [
        'березовый',
        'хвойный',
        'смешанный',
    ]
