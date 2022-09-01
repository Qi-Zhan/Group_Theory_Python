import unittest
from src.utils import *


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


if __name__ == '__main__':
    unittest.main()
