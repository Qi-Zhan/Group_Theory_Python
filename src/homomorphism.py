from __future__ import annotations
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
        ker(f) = { u ∈ G: f(u) = e }
        kernel will always be a normal subgroup of G
        :return: kernel of the homomorphism
        """
        return {i for i in self._G if self._map[i] == self._H.eye()}

    def image(self) -> Set[GroupElement]:
        """
        img(h) = { h(u) : u ∈ G }
        image always be a subgroup if H
        :return: image of the homomorphism
        """
        return {self._map[i] for i in self._G}

    def first_isomorphism_theorem(self) -> Homomorphism:
        """
        f : G -> H be a homomorphism, then
        1) the kernel is a normal subgroup of G
        2) the image is a subgroup of H
        3) the image is isomorphic to the quotient group G/ker
        :return: the isomorphism
        """
        ker = self.kernel()
        img = self.image()
        quotient_group = self._G.quotient(ker)
        assert quotient_group is not False  # kernel must be a normal subgroup so quotient must exist
        img = self._H.can_be_subgroup(img)
        assert img is not False  # image must be a subgroup
        new_map = {}
        for element in quotient_group:  # g(aN) = g(a)
            new_map[element] = self._map[element.value()]
        hom = Homomorphism(quotient_group, img, new_map)
        assert hom.is_isomorphism() is True
        return hom

    def maps_to(self, g: GroupElement) -> GroupElement:
        return self._map[g]

    def G(self) -> Group:
        return self._G

    def H(self) -> Group:
        return self._H

    def check_homomorphism(self, maps: Dict[GroupElement, GroupElement], G: Group, H: Group) -> bool:
        pass

    def print_table(self):
        for key in self._map:
            print(key, "->", self._map[key])
