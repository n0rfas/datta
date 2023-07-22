from abc import ABC
from random import choice, randint


class BaseTerrain(ABC):

    _title = ''
    _emoji_icon = '❌'
    _transit_time = 0
    _rarity = 0
    _seed_list = []
    _seed = ''
    _inhabitants = []

    was_visited = False

    def __init__(self) -> None:
        super().__init__()
        self._seed = choice(self._seed_list)

    @classmethod
    def rarity(cls):
        return cls._rarity

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return f'{self._seed} {self.title}'

    @property
    def emoji_icon(self) -> str:
        if self.was_visited:
            return self._emoji_icon
        else:
            return '🌫'

    @property
    def transit_time(self) -> int:
        return self._transit_time

    @property
    def seed(self) -> str:
        return self._seed

    def meet(self):
        if randint(0, 1) == 1:
            return self._inhabitants[0]()
        else:
            return None
