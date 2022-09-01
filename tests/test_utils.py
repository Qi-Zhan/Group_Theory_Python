import unittest
from src.utils import *
from src.group_element import Integer


class IsPrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(97), True)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(91), False)
        self.assertEqual(is_prime(49), False)


class PermuteTest(unittest.TestCase):
    def test_basic(self):
        f = (1, 3, 2)
        g = (2, 1, 3)
        self.assertEqual((2, 3, 1), permute(f, g))
        self.assertEqual((3, 1, 2), permute(g, f))


class FactorTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(factor(2), [1, 2])
        self.assertEqual(factor(10), [1, 2, 5, 10])


class PowerSetTest(unittest.TestCase):
    def test_basic(self):
        ps = power_set({Integer(1), Integer(2), Integer(3)})
        a1 = Integer(1)
        a2 = Integer(2)
        a3 = Integer(3)
        self.assertIn((a1, a2, a3), ps)
        self.assertIn((a1, a2), ps)
        self.assertIn((a1, a3), ps)
        self.assertIn((a2, a3), ps)
        self.assertIn((), ps)

    def test_empty(self):
        pass
        # self.assertEqual(power_set(set()), set())


if __name__ == '__main__':
    unittest.main()
