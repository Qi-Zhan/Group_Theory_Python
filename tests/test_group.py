import unittest

from src.std_group_lib import *


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

    def test_normal_subgroup_trivial(self):
        group = CyclicGroup(10)
        normal = group.can_be_normal_subgroup({Integer(0), Integer(5)})
        self.assertNotEqual(False, normal)

    def test_normal_subgroup_nontrivial(self):
        group = SymmetricGroup(3)
        normal = group.can_be_normal_subgroup({Permutation((1, 2, 3)), Permutation((2, 3, 1)), Permutation((3, 1, 2))})
        self.assertNotEqual(False, normal)
        self.assertIn(normal, group.nontrivial_subgroups())
        s = {Permutation((1, 2, 3)), Permutation((1, 3, 2))}
        self.assertNotEqual(False, group.can_be_subgroup(s))
        self.assertEqual(False, group.can_be_normal_subgroup(s))

    def test_cyclic(self):
        s = set()
        for i in range(10):
            s.add(Integer(i))
        g1 = Group(s, Modulo(10), Integer(0))
        print(g1)
        self.assertEqual(len(g1.subgroups()), 4)
        self.assertEqual(len(g1.normal_subgroups()), 4)
        self.assertEqual(len(g1.nontrivial_subgroups()), 2)

    def test_permutation(self):
        pass


class DihedralGroupTest(unittest.TestCase):
    def test_odd(self):
        G = DihedralGroup(3)
        self.assertEqual(G.order(), 6)
        self.assertEqual(len(G.nontrivial_subgroups()), 4)

    def test_even(self):
        G = DihedralGroup(4)
        self.assertEqual(8, G.order())


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
        G = SymmetricGroup(3)
        self.assertEqual(2, G.generate([Permutation((2, 1, 3))]).order())
        self.assertEqual(3, G.generate([Permutation((2, 3, 1))]).order())
        self.assertEqual(1, G.generate([Permutation((1, 2, 3))]).order())


class ProductGroupTest(unittest.TestCase):
    def test_basic(self):
        g = ProductGroup([CyclicGroup(2), CyclicGroup(2)])
        self.assertEqual(4, g.order())


class QuotientGroupTest(unittest.TestCase):
    def test_klein(self):
        G = SymmetricGroup(4)
        N = {Permutation((1, 2, 3, 4)), Permutation((2, 1, 4, 3)), Permutation((3, 4, 1, 2)), Permutation((4, 3, 2, 1))}
        G_mod_N = G.quotient(N)
        self.assertEqual(G_mod_N.order(), G.order() // len(N))  # Lagrange Theorem

    def test_basic(self):
        G = CyclicGroup(10)
        G_mod_N = G.quotient({Integer(0), Integer(5)})
        self.assertEqual(2, G.order() // G_mod_N.order())  # Lagrange Theorem
        G_mod_N = G.quotient(G.elements())  # G / G = {e}
        self.assertEqual(1, G_mod_N.order())


if __name__ == '__main__':
    unittest.main()
