from abc import ABC, abstractmethod
from typing import Dict
from .group_element import GroupElement
from .abstract_group import AbstractGroup


class Homomorphism(ABC):
    """ homomorphism  G -> H
    """

    @abstractmethod
    def map(self) -> Dict[GroupElement, GroupElement]:
        pass

    @abstractmethod
    def kernel(self) -> GroupElement:
        pass

    @abstractmethod
    def image(self) -> [GroupElement]:
        pass

    @abstractmethod
    def maps_to(self, g: GroupElement) -> GroupElement:
        pass

    @abstractmethod
    def G(self) -> AbstractGroup:
        pass

    def H(self) -> AbstractGroup:
        pass


def check_homomorphism(maps: Dict[GroupElement, GroupElement], G: AbstractGroup, H: AbstractGroup) -> bool:
    return False
