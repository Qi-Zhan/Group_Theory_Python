import unittest
from src.group import Group
from src.std_group_lib import CyclicGroup, SymmetricGroup, ProductGroup
from src.group_element import Integer
from src.binaryop import Modulo


class GroupOperatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._s = set()
        for i in range(10):
            self._s.add(Integer(i))

    def test_modulo(self):
        g1 = Group(self._s, Modulo(10), Integer(0))
        g2 = CyclicGroup(10)
        self.assertEqual(g1.order(), g2.order())
        self.assertEqual(True, g1.is_abel())
        for g in g1.elements():
            self.assertIn(g, g2.elements())

    def test_modulo_plus(self):
        try:
            Group(self._s, Modulo(10, "MULTI"), Integer(1))
        except AssertionError:
            pass
        else:
            self.assertEqual(False, True)
        s = set()
        for i in range(1, 7):
            s.add((Integer(i)))
        g = Group(s, Modulo(7, "MULTI"), Integer(1))
        self.assertEqual(g.inverse(Integer(3)), Integer(5))

    def test_group_equal(self):
        self.assertEqual(CyclicGroup(10), Group(self._s, Modulo(10), Integer(0)))
        self.assertNotEqual(CyclicGroup(8), Group(self._s, Modulo(10), Integer(0)))


class SubGroupTestCase(unittest.TestCase):
    def test_left_right_coset_equal(self):
        group = CyclicGroup(10)
        a = group.left_coset(Integer(1), group.elements())
        b = group.right_coset(Integer(2), group.elements())
        self.assertEqual(a, b)

    def test_left_right_coset_non_equal(self):
        # TODO klein4 in S4
        pass

    def test_normal_subgroup(self):
        s = set()
        for i in range(10):
            s.add(Integer(i))
        g1 = Group(s, Modulo(10), Integer(0))
        subgroups = g1.subgroups()

    def test_cyclic(self):
        s = set()
        for i in range(10):
            s.add(Integer(i))
        g1 = Group(s, Modulo(10), Integer(0))
        self.assertEqual(len(g1.subgroups()), 4)
        self.assertEqual(len(g1.normal_subgroups()), 4)
        self.assertEqual(len(g1.nontrivial_subgroups()), 2)

    def test_permutation(self):
        pass

    def test_time(self):
        pass
        # s = set()
        # for i in range(20):
        #     s.add(Integer(i))
        # g1 = Group(s, Modulo(20), Integer(0))
        # subgroups = g1.subgroups()


class GenerateTest(unittest.TestCase):
    def test_cyclic_generate_all(self):
        """
        every non identity element in prime order cyclic group is generator
        """
        G = CyclicGroup(7)
        for i in range(1, 7):
            H = G.generate([Integer(i)])
            self.assertEqual(G, H)

    def test_permutation_generate_some(self):
        pass


class ProductGroupTest(unittest.TestCase):
    def test_basic(self):
        g = ProductGroup([CyclicGroup(2), CyclicGroup(2)])
        self.assertEqual(4, g.order())


if __name__ == '__main__':
    unittest.main()
