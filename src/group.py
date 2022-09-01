from __future__ import annotations
from .binaryop import Operator
from .group_element import GroupElement
from typing import Set, List
from .utils import power_set


class Group:
    def __init__(self, s: Set[GroupElement], bop: Operator, e: GroupElement):
        assert e in s
        self._e = e
        self._s = s
        self._bop = bop
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
        l: List[Group] = []
        for s in power_set(self._s):
            try:
                g = Group(set(s), self._bop, self._e)
            except AssertionError:
                continue
            else:
                l.append(g)
        return l

    def normal_subgroups(self) -> [Group]:
        if self.is_abel():
            return self.subgroups()
        else:
            raise NotImplemented

    def nontrivial_subgroups(self) -> [Group]:
        return [g for g in self.subgroups() if g.order() != 1 and g.order() != self.order()]

    def elements(self) -> Set[GroupElement]:
        return self._s

    def bop(self, g: GroupElement, h: GroupElement) -> GroupElement:
        return self._op(g, h)

    def visualize(self):
        pass

    def is_abel(self):
        for i in self._s:
            for j in self._s:
                if self._op(i, j) != self._op(j, i):
                    return False
        return True

    def __str__(self):
        s = [str(e) for e in self._s]
        return "{" + ",".join(s) + "}"

    def __eq__(self, other):
        if isinstance(other, Group):
            if other.order() != self.order():
                return False
            if other._bop != self._bop:
                return False
            for element in self._s:
                if element not in other._s:
                    return False
            return True
        return False
