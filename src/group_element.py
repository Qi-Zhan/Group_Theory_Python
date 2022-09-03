from __future__ import annotations
from abc import abstractmethod, ABC
from typing import Tuple, Set


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
    def __repr__(self):
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
        return False

    def __hash__(self):
        return hash(self._p)

    def __str__(self):
        return str(self._p)

    def __repr__(self):
        return str(self._p)


class Word(GroupElement):
    def __repr__(self):
        return self._s

    def value(self) -> str:
        return self._s

    def __init__(self, s: str):
        self._s = s

    def __str__(self):
        return self._s

    def __hash__(self):
        return hash(self._s)

    def __eq__(self, other):
        if isinstance(other, Word):
            return self._s == other._s
        return False


class ProductElement(GroupElement):
    def value(self) -> Tuple[GroupElement, ...]:
        return self._p

    def __init__(self, elements: Tuple[GroupElement, ...]):
        self._p = elements

    def __str__(self):
        return str(self._p)

    def __hash__(self):
        return hash(str(self._p))

    def __eq__(self, other):
        if isinstance(other, ProductElement):
            for i in range(len(self._p)):
                if self._p[i] != other._p[i]:
                    return False
            return True
        return False

    def __repr__(self):
        return str(self._p)


class QuotientElement(GroupElement):
    def value(self) -> GroupElement:
        return self._repr

    def normal_elements(self) -> Set[GroupElement]:
        return self._s

    def __init__(self, rep: GroupElement, s: Set[GroupElement]):
        self._s = s  # N normal subgroup
        self._repr = rep  # aN

    def __str__(self):
        return str(self._repr)

    def __repr__(self):
        return self._s

    def __hash__(self):
        return hash(self._repr)

    def __eq__(self, other):
        if isinstance(other, QuotientElement):
            if other._repr in self._s and self._repr in other._s:
                return True
        return False
