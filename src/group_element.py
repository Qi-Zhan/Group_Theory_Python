from __future__ import annotations
from abc import abstractmethod, ABC


class GroupElement(ABC):
    @abstractmethod
    def value(self):
        pass


class Integer(GroupElement):
    def __init__(self, i: int):
        self._i = i

    def value(self) -> int:
        return self._i

    def __eq__(self, other):
        if isinstance(other, Integer):
            return other.value() == self.value()
        return False

    def __str__(self):
        return str(self._i)

class Permute(GroupElement):
    pass

