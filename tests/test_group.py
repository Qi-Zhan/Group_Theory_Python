import unittest
from src.group import Group
from src.cyclic_group import CyclicGroup
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
    def test_cyclic(self):
        s = set()
        for i in range(10):
            s.add(Integer(i))
        g1 = Group(s, Modulo(10), Integer(0))
        subgroups = g1.subgroups()
        for subgroup in subgroups:
            print(subgroup)
        for subgroup in g1.nontrivial_subgroups():
            print(subgroup)

    def test_permutation(self):
        pass

    def test_time(self):
        pass
        # s = set()
        # for i in range(20):
        #     s.add(Integer(i))
        # g1 = Group(s, Modulo(20), Integer(0))
        # subgroups = g1.subgroups()


if __name__ == '__main__':
    unittest.main()
