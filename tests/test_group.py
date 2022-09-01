import unittest
from src.group import Group
from src.cyclic_group import CyclicGroup
from src.group_element import Integer
from src.binaryop import Modulo


class GroupTestCase(unittest.TestCase):
    def test_modulo(self):
        s = set()
        for i in range(10):
            s.add(Integer(i))
        g1 = Group(s, Modulo(10), Integer(0))
        g2 = CyclicGroup(10)
        self.assertEqual(g1.order(), g2.order())
        self.assertEqual(True, g1.is_abel())
        for g in g1.elements():
            self.assertIn(g, g2.elements())


if __name__ == '__main__':
    unittest.main()
