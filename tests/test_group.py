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
        Group(s, Modulo(10), Integer(0))
        CyclicGroup(10)


if __name__ == '__main__':
    unittest.main()
