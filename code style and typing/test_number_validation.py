import unittest
import number_validation


class TestNumber_Validation(unittest.TestCase):

    def test_number_validation(self):
        """Testing number_validation func with different attrs."""
        self.assertEqual(number_validation.number_validation('1', '0'), ('1', '0'))
        self.assertEqual(number_validation.number_validation('5.0', '6'), ('5.0', '6'))
        self.assertEqual(number_validation.number_validation('6', 'ababjasj'), False)


if __name__ == '__main__':
    unittest.main()
