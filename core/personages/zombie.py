from .base import BasePersonage


class Zombie(BasePersonage):

    _title = 'живой мертвец'
    _seed = ['гнилой', 'зеленый', 'склизкий']

    _current_health: 5
    _maximum_health: 10

    _min_damage: 1
    _max_damage: 3

    _min_reward: 1
    _max_reward: 2
