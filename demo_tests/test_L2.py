import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator(8,2)
    
    
    def test_sum(self):
        self.assertEqual(self.calc.sum(),10,"The answer was not 10")

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(),6,"The answer was not 6")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(),16,"The answer was not 16")

    def test_divide(self):
        self.assertEqual(self.calc.division(),4,"The answer was not 4")

if __name__ == "__main__":
    unittest.main()