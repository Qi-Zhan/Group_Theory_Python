"""
This file provides some basic group implemented by class Group in group.py
* CyclicGroup
Z(n) = {0, 1, ..., n-1} (+ mod n)
* SymmetricGroup
* PermutationGroup
* ProductGroup
* QuotientGroup
...
"""
from .group import Group
from .group_element import GroupElement, Integer, Permutation
from .binaryop import Modulo, Operator, Permute
from .utils import factor, all_permutations


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
    def __init__(self, n: int):
        assert n >= 1, "n must be positive integer"
        self._n = n
        e = range(1, n + 1)
        s = set([Permutation(i) for i in all_permutations(n)])
        super(SymmetricGroup, self).__init__(s, Permute(), Permutation(tuple(e)))

    def is_abel(self):
        return self._n == 1

    def __str__(self):
        return "S(" + str(self._n) + ")"


class PermutationGroup(Group):
    def __init__(self, generators: [Permutation]):
        pass


class KleinFourGroup(Group):
    """

    """
    # TODO Z2 * Z2 ~ klein klein group in permutation
    def __init__(self):
        pass

    def order(self) -> int:
        return 4

    def is_abel(self):
        return True


class ProductGroup(Group):
    def __init__(self, groups: [Group]):
        # TODO
        pass


class QuotientGroup(Group):
    def __init__(self):
        # TODO
        pass
