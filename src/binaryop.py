from abc import ABC, abstractmethod
from .group_element import Integer, GroupElement


class Operator(ABC):
    @abstractmethod
    def op(self, g: GroupElement, h: GroupElement) -> GroupElement:
        pass


class Modulo(Operator):
    def __init__(self, m: int):
        self._m = m

    def op(self, g: Integer, h: Integer) -> Integer:
        return Integer((g.value() + h.value()) % self._m)



