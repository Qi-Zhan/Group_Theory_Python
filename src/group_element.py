from __future__ import annotations
from abc import abstractmethod, ABC


class GroupElement(ABC):
    pass


class Integer(GroupElement):
    def __init__(self, i: int):
        self._i = i

    def __str__(self):
        return str(self._i)



class Permute(GroupElement):
    pass

