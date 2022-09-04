import unittest
from src.group import *
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

    def test_klein(self):
        # TODO
        pass


if __name__ == '__main__':
    unittest.main()
