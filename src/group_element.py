from __future__ import annotations
from abc import abstractmethod, ABC
from typing import Tuple


class GroupElement(ABC):
    """
    This class provides a virtual group element can be implemented by many ways
    """
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
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

    def __hash__(self):
        return hash(self._i)

    def __str__(self):
        return str(self._i)

    def __repr__(self):
        return str(self._i)


class Permutation(GroupElement):
    def __init__(self, p: Tuple[int]):
        self._p = p

    def value(self) -> Tuple[int]:
        return self._p

    def __eq__(self, other):
        if isinstance(other, Permutation):
            return other.value() == self.value()

    def __hash__(self):
        return hash(self._p)

    def __str__(self):
        return str(self._p)


class Word(GroupElement):
    def value(self):
        return self._s

    def __init__(self, s: str):
        self._s = s
        pass

    def __str__(self):
        return self._s

    def __hash__(self):
        return hash(self._s)

    def __eq__(self, other):
        pass