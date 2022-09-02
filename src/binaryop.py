"""
TODO
"""
from abc import ABC, abstractmethod
from .group_element import Integer, GroupElement, Permutation
from .utils import permute


class Operator(ABC):
    @abstractmethod
    def op(self, g: GroupElement, h: GroupElement) -> GroupElement:
        pass

# class


class Modulo(Operator):
    def __init__(self, m: int, c="PLUS"):
        self._m = m
        self._c = c
        if c == "PLUS":
            self._op = lambda x, y: (x + y) % self._m
        elif c == "MULTI":
            self._op = lambda x, y: (x * y) % self._m
        else:
            raise NotImplemented

    def op(self, g: Integer, h: Integer) -> Integer:
        return Integer(self._op(g.value(), h.value()))

    def __eq__(self, other):
        if isinstance(other, Modulo):
            if other._c == self._c and other._m == self._m:
                return True
        return False

    def __str__(self):
        if self._c == "PLUS":
            return "+ mod " + str(self._m)
        elif self._c == "MULTI":
            return "* mod " + str(self._m)
        else:
            raise NotImplemented


class Permute(Operator):

    def op(self, g: Permutation, h: Permutation) -> Permutation:
        return Permutation(permute(g.value(), h.value()))

    def __eq__(self, other):
        if isinstance(other, Permute):
            return True
        return False

    def __str__(self):
        return "permutation"
