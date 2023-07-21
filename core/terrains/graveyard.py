from .base import BaseTerrain
from core.personages.zombie import Zombie


class Graveyard(BaseTerrain):

    _title = 'Кладбище'
    _emoji_icon = '🪦 '
    _transit_time = 2
    _rarity = 1
    _seed_list = [
        'Старое',
        'Ухоженное',
        'Мрачное',
    ]

    _inhabitants = [Zombie]
