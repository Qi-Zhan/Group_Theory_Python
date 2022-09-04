from __future__ import annotations

from typing import Set, List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np

from .binaryop import Operator, Quotient
from .group_element import GroupElement, QuotientElement
from .utils import power_set


class Group:
    """
    This class provides a general group class with many corresponding operation on a group.
    Generally, a group is a set and an operation that combines tow elements of the set
    to produce a third element of the set which satisfies:
    0) associativity: (gh)j = g(hj)
    1) exists identity e: ge = eg = g
    2) for any element g exists inverse g-1 s.t. g g-1 = g-1 g = e
    """
    def __init__(self, s: Set[GroupElement], bop: Operator, e: GroupElement):
        """
        Check the set and corresponding operation satisfy the condition to be a group
        :param s: set of elements
        :param bop: binary operation
        :param e: identity
        """
        assert e in s
        self._e = e
        self._s = s
        self._bop = bop
        self._op = bop.op
        self.check_e()
        self.check_inverse()
        self.check_closed()
        # self.check_assoc()

    def check_closed(self) -> None:
        for i in self._s:
            for j in self._s:
                assert self._op(i, j) in self._s, ("element ", i, j, "do not in set")

    def check_assoc(self) -> None:
        for i in self._s:
            for j in self._s:
                for k in self._s:
                    g = self._op(i, self._op(j, k))
                    h = self._op(self._op(i, j), k)
                    assert h == g, "violate associativity"

    def check_inverse(self) -> None:
        for i in self._s:
            flag = False
            for j in self._s:
                if self._op(i, j) == self._e:
                    flag = True
                    break
            assert flag, ("element " + str(i) + "does not have inverse")

    def check_e(self) -> None:
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
        """
        The number of elements in a group is called the order of the group
        """
        return len(self._s)

    def table(self) -> Tuple[List[List[str]], List[str], List[str]]:
        l_set = list(self._s)
        l_set.remove(self._e)
        l_set.insert(0, self._e)
        compute = []
        for i in l_set:
            temp = []
            for j in l_set:
                temp.append(str(self._op(i, j)))
            compute.append(temp)
        l_str = [str(i) for i in l_set]
        return compute, l_str, l_str

    def print_table(self) -> None:
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        cell_text, row_header, col_header = self.table()
        rcolor = plt.cm.BuPu(np.full(len(row_header), 0.1))
        ccolor = plt.cm.BuPu(np.full(len(col_header), 0.1))
        ax.table(cellText=cell_text, rowLabels=row_header, colLabels=col_header,
                 rowColours=rcolor, colColours=ccolor, cellLoc='center', loc='center')
        fig.tight_layout()
        plt.show()

    def subgroups(self) -> [Group]:
        """
        A subgroup is a subset of group elements of a group, which is a group itself
        :return: all subgroups in this group by brute force
        """
        l: List[Group] = []
        for s in power_set(self._s):
            try:
                g = Group(set(s), self._bop, self._e)
            except AssertionError:
                continue
            else:
                l.append(g)
        return l

    def can_be_subgroup(self, s: Set[GroupElement]) -> Union[bool, Group]:
        """
        :param s: set of some elements
        :return: return the subgroup if can be, False otherwise
        """
        try:
            g = Group(set(s), self._bop, self._e)
        except AssertionError:
            return False
        else:
            return g

    def left_coset(self, g: GroupElement, N: Set[GroupElement]) -> Set[GroupElement]:
        """
        :param g: element
        :param N: subset
        :return: gN = {gn : n ∈ N}
        """
        return set([self._op(g, n) for n in N])

    def right_coset(self, g: GroupElement, N: Set[GroupElement]) -> Set[GroupElement]:
        """
        :param g: element
        :param N: subset
        :return: Ng = {ng : n ∈ N}
        """
        return set([self._op(n, g) for n in N])

    def cosets(self, N: Set[GroupElement]) -> [Set[GroupElement]]:
        cosets_ = []
        for g in self._s:
            left = self.left_coset(g, N)
            if left not in cosets_:
                cosets_.append(left)
        return cosets_

    def normal_subgroups(self) -> [Group]:
        """
        A normal subgroup is a subgroup N, for any element g in G, gN = Ng in set meaning
        see definition of gN and Ng in left_coset and right_coset
        Notion: N ◁ G
        :return: all normal subgroups in the group
        """
        if self.is_abel():  # subgroup in abel group must be normal subgroup
            return self.subgroups()
        else:
            subgroups = self.subgroups()
            l: [Group] = []
            for subgroup in subgroups:
                flag = True
                for g in self:
                    if g in subgroup:
                        continue
                    else:
                        if self.left_coset(g, subgroup.elements()) != self.right_coset(g, subgroup.elements()):
                            flag = False
                            break
                if flag:
                    l.append(subgroup)
            return l

    def can_be_normal_subgroup(self, N: Set[GroupElement]) -> Union[bool, Group]:
        """
        :param N: set of some elements
        :return: return the normal subgroup if the set can be, False otherwise
        """
        try:
            group = Group(set(N), self._bop, self._e)
        except AssertionError:
            return False
        else:
            for g in self._s:
                # print(g, self.left_coset(g, N), self.right_coset(g, N))
                if self.left_coset(g, N) != self.right_coset(g, N):
                    return False
            return group

    def nontrivial_subgroups(self) -> [Group]:
        """
        nontrivial subgroup is a subgroup which is not identity group or the whole group itself
        :return:
        """
        return [g for g in self.subgroups() if g.order() != 1 and g.order() != self.order()]

    def elements(self) -> Set[GroupElement]:
        return self._s

    def operator(self) -> Operator:
        return self._bop

    def bop(self, g: GroupElement, h: GroupElement) -> GroupElement:
        return self._op(g, h)

    def visualize(self):
        raise NotImplemented

    def quotient(self, N: Set[GroupElement]) -> Union[Group, bool]:
        N = self.can_be_normal_subgroup(N)
        if not N:
            return False
        cosets_ = self.cosets(N.elements())
        new_elements = set([QuotientElement(next(iter(i)), N.elements(), self._bop) for i in cosets_])
        e = QuotientElement(self._e, self.left_coset(self._e, N.elements()), self._bop)
        G_mod_N = Group(new_elements, Quotient(self._bop), e)
        return G_mod_N

    def is_abel(self) -> bool:
        """
        A group is called abel group if for all a, b in group, ab = ba (commutativity)
        :return:
        """
        for i in self._s:
            for j in self._s:
                if self._op(i, j) != self._op(j, i):
                    return False
        return True

    def generate(self, generators: [GroupElement]) -> Group:
        """
        A group is called generated by generators if it is the smallest group containing those elements
        :param generators:
        :return: group generated by generators
        """
        assert len(generators) > 0
        for generator in generators:
            assert generator in self._s
        diff = True
        s = set(generators)
        temp = set()
        while diff:
            diff = False
            temp.clear()
            for a in s:
                for b in s:
                    ab = self._op(a, b)
                    ba = self._op(b, a)
                    if ab not in s:
                        temp.add(ab)
                        diff = True
                    if ba not in s:
                        temp.add(ba)
                        diff = True
            s.update(temp)
        return Group(s, self._bop, self._e)

    def __iter__(self):
        return self._s.__iter__()

    def __contains__(self, item):
        return item in self._s

    def __str__(self):
        s = ",".join([str(e) for e in self._s])
        return f"{{{s}}} under {self._bop}"

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
