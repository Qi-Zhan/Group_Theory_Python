"""
This file provides some basic group implemented by group.py
* CyclicGroup
G = (a)
* SymmetricGroup
* ProductGroup
* QuotientGroup
...
"""
from .group import Group
from .group_element import GroupElement, Integer, Permutation
from .binaryop import Modulo, Operator
from .utils import factor, permute


class CyclicGroup(Group):
    def __init__(self, order: int) -> None:
        assert order >= 1, "order must be positive integer"
        s = set([Integer(i) for i in range(order)])
        super(CyclicGroup, self).__init__(s, Modulo(order), Integer(0))

    def subgroups(self) -> [Group]:
        factor_list = factor(self.order())
        return [CyclicGroup(i) for i in factor_list]

    def is_abel(self):
        return True

    def __str__(self):
        return "Z(" + str(self.order()) + ")"


class SymmetricGroup(Group):
    pass


class ProductGroup(Group):
    def __init__(self, groups: [Group]):
        # TODO
        pass


class QuotientGroup(Group):
    def __init__(self):
        # TODO
        pass