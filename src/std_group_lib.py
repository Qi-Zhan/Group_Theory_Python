"""
This file provides some basic group implemented by class Group in group.py
* CyclicGroup
Z(n) = {0, 1, ..., n-1} (+ mod n)
* SymmetricGroup
* PermutationGroup
* ProductGroup
* QuotientGroup
* DihedralGroup
...
"""
from .binaryop import Modulo, Permute, Product
from .group import Group
from .group_element import Integer, Permutation, ProductElement
from .utils import *


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
        return f"Z({self.order()})"


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
        return f"S({self._n})"


class PermutationGroup(Group):
    def __init__(self, generators: [Permutation]):
        pass


class ProductGroup(Group):
    def __init__(self, groups: [Group]):
        self._groups: [Group] = groups
        eye = map(lambda x: x.eye(), groups)
        eye = ProductElement(tuple(eye))
        elements = map(lambda x: x.elements(), groups)
        elements = cartesian_product(elements)
        elements = set([ProductElement(i) for i in elements])
        op = map(lambda x: x.operator(), groups)
        op = Product(tuple(op))
        super(ProductGroup, self).__init__(elements, op, eye)

    def order(self) -> int:
        return reduce_multi([x.order() for x in self._groups])

    def is_abel(self) -> bool:
        for g in self._groups:
            if not g.is_abel():
                return False
        return True


class KleinFourGroup(ProductGroup):
    """
    The smallest non cyclic group
        e a b c
    e   e a b c
    a   a e c b
    b   b c e a
    c   c b a e
    """

    def __init__(self, type_="permute"):
        super(KleinFourGroup, self).__init__([CyclicGroup(2), CyclicGroup(2)])

    def order(self) -> int:
        return 4

    def is_abel(self):
        return True


class DihedralGroup(Group):
    """
    A Dihedral Group is the group of symmetries of a regular polygon,
    which contains reflection and rotation.
    Dn = <r, s| r^n = s^2 = (sr)^2 =1>
    """
    def __init__(self, n: int):
        self._n = n
        rotation = {Permutation(rotation_n(i, n)) for i in range(n)}
        reflection = {Permutation(reflection_n(i, n)) for i in range(1, n + 1)}
        super(DihedralGroup, self).__init__(rotation.union(reflection), Permute(),
                                            Permutation(tuple([i for i in range(1, n+1)])))

    def is_abel(self) -> bool:
        return self._n <= 2

    def order(self) -> int:
        assert len(self._s) == 2 * self._n
        return 2 * self._n

    def __str__(self):
        return f"D({self._n})"
