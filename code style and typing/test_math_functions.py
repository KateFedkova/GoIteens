import unittest
import math_functions


class TestMath_Functions(unittest.TestCase):

    def test_add_func(self):
        """Testing add func with different attrs."""
        self.assertEqual(math_functions.add_func(1, 2), 3)
        self.assertEqual(math_functions.add_func(8.5, 4.7), 13.2)
        self.assertEqual(math_functions.add_func(4.0, 2.0), 6)

    def test_sub_func(self):
        """Testing subtract func with different attrs."""
        self.assertEqual(math_functions.sub_func(20, 10), 10)
        self.assertEqual(math_functions.sub_func(-7, 5), -12.0)
        self.assertEqual(math_functions.sub_func(8, -8), 16)

    def test_multiply(self):
        """Testing multiply func with different attrs."""
        self.assertEqual(math_functions.mul_func(5, 10), 50)
        self.assertEqual(math_functions.mul_func(-5, 2), -10)
        self.assertEqual(math_functions.mul_func(-3, 0), 0)

    def test_divide_success(self):
        """Testing divide func with different attrs.
        If second number is 0, div_func won't be triggered """
        self.assertEqual(math_functions.div_func(5, 5.0), 1)
        self.assertEqual(math_functions.div_func(-10, 5), -2)
        self.assertEqual(math_functions.div_func(-3, -3), 1)
        self.assertEqual(math_functions.div_func(7, 2), 3.5)


if __name__ == '__main__':
    unittest.main()