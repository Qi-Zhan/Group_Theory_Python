from typing import Dict
from .group_element import GroupElement
from .group import Group


class Homomorphism:
    """ homomorphism  G -> H
    """

    def map(self) -> Dict[GroupElement, GroupElement]:
        pass

    def kernel(self) -> GroupElement:
        pass

    def image(self) -> [GroupElement]:
        pass

    def maps_to(self, g: GroupElement) -> GroupElement:
        pass

    def G(self) -> Group:
        pass

    def H(self) -> Group:
        pass

    def check_homomorphism(self, maps: Dict[GroupElement, GroupElement], G: Group, H: Group) -> bool:
        pass
