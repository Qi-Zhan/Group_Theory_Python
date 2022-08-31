from .abstract_group import AbstractGroup
from .group_element import GroupElement, Integer
from .binaryop import Modulo


class CyclicGroup(AbstractGroup):
    def __init__(self, order: int) -> None:
        assert (order >= 1, "order must be positive integer")
        self._order = order
        self._elements = [Integer(i) for i in range(order)]
        self._op = Modulo(order-1)
        self._e = Integer(0)

    def eye(self) -> GroupElement:
        return self._e

    def inverse(self, g: GroupElement) -> GroupElement:
        pass

    def order(self) -> int:
        return self._order

    def table(self):
        pass

    def print_table(self) -> None:
        pass

    def subgroups(self) -> [AbstractGroup]:
        pass

    def normal_subgroups(self) -> [AbstractGroup]:
        pass

    def nontrivial_subgroups(self) -> [AbstractGroup]:
        sgs = self.nontrivial_subgroups()
        return sgs

    def elements(self) -> [Integer]:
        return self._elements

    def bop(self, g: Integer, h: Integer) -> GroupElement:
        return self._op.op(g, h)

    def visualize(self):
        pass

    def __str__(self):
        return "Z("+str(self._order)+")"
