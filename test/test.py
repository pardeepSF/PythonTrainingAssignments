
import unittest
import sys
sys.path.insert(0,'../')
from calculations import Calculations

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.calculation = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 10, 'The sum is correct.')
        self.assertNotEqual(self.calculation.get_sum(), 5, 'The sum is not equal to 5.')

    def test_diff(self):
        self.assertEqual(self.calculation.get_difference(), 6, 'The difference is correct.')
        self.assertNotEqual(self.calculation.get_difference(), 2, 'The difference is not equal to 2.')

    def test_product(self):
        self.assertEqual(self.calculation.get_product(), 16, 'The product is correct.')
        self.assertNotEqual(self.calculation.get_product(), 10, 'The product is not equal to 10.')

    def test_quotient(self):
        self.assertEqual(self.calculation.get_quotient(), 4, 'The quotient is correct.')
        self.assertNotEqual(self.calculation.get_quotient(), 3, 'The division is not equal to 3.')
        self.calc = Calculations(7,0)
        self.assertEqual(self.calc.get_quotient(), 'Can\'t divide with zero', 'The division is wrong.')


if __name__ == '__main__':
    unittest.main()