#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """UNIT TESTING"""
    def test_max_int(self):
        self.assertEqual(max_integer([3, 2, 0, 1]), 3)
        self.assertEqual(max_integer([3, 2, 0, 8]), 8)
        self.assertEqual(max_integer([3, 2, 9, 1, 5]), 9)
        self.assertEqual(max_integer([-3, -2, -10, -1]), -1)
        self.assertEqual(max_integer([3]), 3)
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
