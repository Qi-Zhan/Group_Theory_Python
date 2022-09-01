from abc import ABC, abstractmethod
from .group_element import Integer, GroupElement, Permutation
from .utils import permute


class Operator(ABC):
    @abstractmethod
    def op(self, g: GroupElement, h: GroupElement) -> GroupElement:
        pass


class Modulo(Operator):
    def __init__(self, m: int, c="PLUS"):
        self._m = m
        if c == "PLUS":
            self._op = lambda x, y: (x + y) % self._m
        elif c == "MULTI":
            self._op = lambda x, y: (x * y) % self._m

    def op(self, g: Integer, h: Integer) -> Integer:
        return Integer(self._op(g.value(), h.value()))


class Permute(Operator):

    def op(self, g: Permutation, h: Permutation) -> Permutation:
        return Permutation(permute(g.value(), h.value()))
