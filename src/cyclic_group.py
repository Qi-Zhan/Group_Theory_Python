from abstract_group import AbstractGroup
from group_element import GroupElement


class CyclicGroup(AbstractGroup):

    def __init__(self, order: int) -> None:
        assert (order >= 1, "order must be positive integer")
        self._order = order
        self._elements = []

    def eye(self) -> GroupElement:
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
        sgs:[AbstractGroup] = self.nontrivial_subgroups()
        return sgs

    def elements(self) -> [GroupElement]:
        return self._elements

    def visualize(self):
        pass

    def __str__(self):
        return "Z("+str(self._order)+")"
