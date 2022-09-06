import context
from src.group_element import Integer, Permutation
from src.homomorphism import Homomorphism
from src.std_group_lib import CyclicGroup, SymmetricGroup
from src.utils import parity_permutation

"""
This Homomorphism is a typical hom from symmetric group to 2 element group {0, 1} or {-1 , 1} 
by map a permutation to its parity.
"""


def main():
    H = CyclicGroup(2)  # {0 , 1} under XOR
    G = SymmetricGroup(4)
    map_ = dict([(Permutation(i.value()), Integer(parity_permutation(i.value()))) for i in G.elements()])
    hom = Homomorphism(G, H, map_)
    print("kernel is ", hom.kernel())
    print("image is all", hom.image())
    iso = hom.first_isomorphism_theorem()
    iso.print_table()


if __name__ == '__main__':
    main()
