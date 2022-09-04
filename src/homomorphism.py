from typing import Dict, Set
from .group_element import GroupElement
from .group import Group


class Homomorphism:
    """ homomorphism  G -> H
    Given two groups G, H, a group homomorphism is from G to H is a function h: G -> H such that
    h(u op v) = h(u) op h(v).
    One can deduce that h(e) = e, h(g-1) = h(g)-1
    Further more,
    """

    def __init__(self, G: Group, H: Group, map_: Dict[GroupElement, GroupElement]):
        assert map_[G.eye()] == H.eye()
        for i in G.elements():
            assert i in map_.keys()
            for j in G.elements():
                assert map_[G.bop(i, j)] == H.bop(map_[i], map_[j])
        self._G = G
        self._H = H
        self._map = map_

    @classmethod
    def build_map(cls):
        pass

    def map(self) -> Dict[GroupElement, GroupElement]:
        return self._map

    def is_surjective(self) -> bool:

        return len(set(self._map.values())) == self.H().order()

    def is_injective(self) -> bool:
        return len(set(self._map.values())) == len(self._map.values())

    def is_isomorphism(self) -> bool:
        return self.is_injective() and self.is_surjective()

    def kernel(self) -> Set[GroupElement]:
        """
        ker(h) = { u ∈ G: h(u) = e }
        ker always be a subgroup of G
        :return: kernel of the homomorphism
        """
        return {i for i in self._H if self._map[i] == self._H.eye()}

    def image(self) -> Set[GroupElement]:
        """
        img(h) = { h(u) : u ∈ G }
        image always be a subgroup if H
        :return: image of the homomorphism
        """
        return {self._map[i] for i in self._G}

    def maps_to(self, g: GroupElement) -> GroupElement:
        return self._map[g]

    def G(self) -> Group:
        return self._G

    def H(self) -> Group:
        return self._H

    def check_homomorphism(self, maps: Dict[GroupElement, GroupElement], G: Group, H: Group) -> bool:
        pass

    def print_table(self):
        pass


