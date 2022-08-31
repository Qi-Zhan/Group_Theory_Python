import unittest
from src.binaryop import Modulo
from src.group_element import Integer


class ModuloTestCase(unittest.TestCase):
    def test_basic(self):
        m = Modulo(7)
        g = Integer(3)
        h = Integer(4)
        self.assertEqual(Integer(0), m.op(g, h))


if __name__ == '__main__':
    unittest.main()
