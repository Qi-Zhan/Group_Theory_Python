from __future__ import annotations

from abc import abstractmethod, ABC

from group_element import GroupElement


class AbstractGroup(ABC):

    @abstractmethod
    def eye(self) -> GroupElement:
        pass

    @abstractmethod
    def inverse(self, g: GroupElement) -> GroupElement:
        pass



    @abstractmethod
    def order(self) -> int:
        pass

    @abstractmethod
    def table(self):
        pass

    @abstractmethod
    def print_table(self) -> None:
        # Use math plot to
        pass

    @abstractmethod
    def normal_subgroups(self) -> [AbstractGroup]:
        pass

    @abstractmethod
    def subgroups(self) -> [AbstractGroup]:
        pass

    @abstractmethod
    def nontrivial_subgroups(self) -> [AbstractGroup]:
        pass

    @abstractmethod
    def elements(self) -> [GroupElement]:
        pass

    @abstractmethod
    def visualize(self):
        pass

