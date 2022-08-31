from __future__ import annotations
from .binaryop import Operator
from .group_element import GroupElement
from typing import Set


class Group:
    def __init__(self, s: Set[GroupElement], bop: Operator, e: GroupElement):
        self._e = e
        self._s = s
        self._op = bop.op
        self.check_closed()
        self.check_e()
        self.check_assoc()
        self.check_inverse()

    def check_closed(self):
        for i in self._s:
            for j in self._s:
                assert self._op(i, j) in self._s, ("element ", i, j, "do not in set")

    def check_assoc(self):
        for i in self._s:
            for j in self._s:
                for k in self._s:
                    g = self._op(i, self._op(j, k))
                    h = self._op(self._op(i, j), k)
                    assert h == g, "violate associativity"

    def check_inverse(self):
        for i in self._s:
            flag = False
            for j in self._s:
                if self._op(i, j) == self._e:
                    flag = True
                    break
            assert flag, ("element " + str(i) + "does not have inverse")

    def check_e(self):
        e = self._e
        for i in self._s:
            assert self._op(i, e) == i, ("element ", i, e, "not equal", i)
            assert self._op(e, i) == i, ("element ", e, i, "not equal", i)

    def eye(self) -> GroupElement:
        return self._e

    def inverse(self, g: GroupElement) -> GroupElement:
        for h in self._s:
            if self._op(g, h) == self._e:
                return h
        assert 0, "unreachable"

    def order(self) -> int:
        return len(self._s)

    def table(self):
        l_set = list(self._s)

    def print_table(self) -> None:

        pass

    def subgroups(self) -> [Group]:
        pass

    def normal_subgroups(self) -> [Group]:
        pass

    def nontrivial_subgroups(self) -> [Group]:
        sgs = self.nontrivial_subgroups()
        return sgs

    def elements(self) -> Set[GroupElement]:
        return self._s

    def bop(self, g: GroupElement, h: GroupElement) -> GroupElement:
        return self._op(g, h)

    def visualize(self):
        pass

    def __str__(self):
        return "Z(" + str(self.order()) + ")"
