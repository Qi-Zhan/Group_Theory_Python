import unittest

from src.homomorphism import *
from src.std_group_lib import *


class HomomorphismTestCase(unittest.TestCase):
    def test_map_to_eye(self):
        G = CyclicGroup(10)
        H = CyclicGroup(1)
        d = dict()
        for e in G:
            d[e] = H.eye()
        hom = Homomorphism(G, H, d)
        self.assertEqual(False, hom.is_injective())
        self.assertEqual(True, hom.is_surjective())
        self.assertNotEqual(False, G.can_be_subgroup(hom.kernel()))
        self.assertNotEqual(False, H.can_be_subgroup(hom.image()))

    def test_isomorphism(self):
        # Actually, one can run code above is to show the correct of the isomorphism
        H = CyclicGroup(2)  # {0 , 1} under XOR
        G = SymmetricGroup(4)
        map_ = dict([(Permutation(i.value()), Integer(parity_permutation(i.value()))) for i in G.elements()])
        hom = Homomorphism(G, H, map_)
        iso = hom.first_isomorphism_theorem()
        self.assertEqual(iso.is_isomorphism(), True)
        self.assertEqual(G.order(), len(hom.kernel()) * len(hom.image()))


if __name__ == '__main__':
    unittest.main()
