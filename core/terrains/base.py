from abc import ABC


class BaseTerrain(ABC):

    _title = ''
    _emoji_icon = '❌'
    _transit_time = 0
    _rarity = 0

    @property
    def title(self) -> str:
        return self._title

    @property
    def emoji_icon(self) -> str:
        return self._emoji_icon

    @property
    def transit_time(self) -> int:
        return self._transit_time
