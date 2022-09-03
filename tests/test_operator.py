import unittest
from src.binaryop import Modulo, Product
from src.group_element import Integer, ProductElement


class ModuloTestCase(unittest.TestCase):
    def test_plus(self):
        m = Modulo(7)
        g = Integer(3)
        h = Integer(4)
        self.assertEqual(Integer(0), m.op(g, h))

    def test_multi(self):
        m = Modulo(7, "MULTI")
        g = Integer(3)
        h = Integer(4)
        self.assertEqual(Integer(5), m.op(g, h))


class ProductTestCase(unittest.TestCase):
    def test_product_modulo(self):
        a1 = Integer(10)
        a2 = Integer(3)
        op = Product((Modulo(5), Modulo(13)))
        res = op.op(ProductElement((a1, a2)), ProductElement((a2, a1)))
        self.assertEqual(res.value(), (Integer(3), Integer(0)))

    def test_product_permute(self):
        pass


if __name__ == '__main__':
    unittest.main()
