from abc import ABC


class BasePersonage(ABC):

    _title: str
    _seed: list[str]

    _current_health: int
    _maximum_health: int

    _min_damage: int
    _max_damage: int

    _min_reward: int
    _max_reward: int

    @property
    def title(self) -> str:
        return self._title
