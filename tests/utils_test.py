import unittest
from src.utils import *


class IsPrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(97), True)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(91), False)
        self.assertEqual(is_prime(49), False)


if __name__ == '__main__':
    unittest.main()
