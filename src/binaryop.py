from abc import ABC, abstractmethod
from .group_element import Integer, GroupElement, Permutation, ProductElement, QuotientElement
from .utils import permute
from typing import Tuple
from itertools import starmap


class Operator(ABC):
    """
    This class provides a virtual binary operators can be implemented by many ways
    """
    @abstractmethod
    def op(self, g: GroupElement, h: GroupElement) -> GroupElement:
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


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


class Product(Operator):
    def __init__(self, ops: Tuple[Operator, ...]):
        self._op: Tuple[Operator] = ops

    def op(self, g: ProductElement, h: ProductElement) -> ProductElement:
        # to check type
        def map_one(g1: GroupElement, g2: GroupElement, op1: Operator) -> GroupElement:
            return op1.op(g1, g2)
        l: Tuple[GroupElement] = tuple(starmap(map_one, zip(g.value(), h.value(), self._op)))
        return ProductElement(l)

    def __eq__(self, other):
        if isinstance(other, Product):
            return

    def __str__(self):
        '*'.join([str(i) for i in self._op])


class Quotient(Operator):
    def __init__(self, op: Operator):
        self._op = op

    def op(self, g: QuotientElement, h: QuotientElement) -> QuotientElement:
        return QuotientElement(self._op.op(g.value(), h.value()), g.normal_elements(), self._op)

    def __eq__(self, other):
        if isinstance(other, Quotient):
            return self._op == other._op
        return False

    def __str__(self):
        return "quotient " + str(self._op)
