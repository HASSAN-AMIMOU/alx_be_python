import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)        # Normal case
        self.assertEqual(self.calc.add(-1, 1), 0)       # Negative number
        self.assertEqual(self.calc.add(0, 0), 0)        # Adding zero

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)   # Normal case
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Negative result
        self.assertEqual(self.calc.subtract(0, 0), 0)   # Subtracting zero

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)      # Normal case
        self.assertEqual(self.calc.multiply(0, 5), 0)      # Multiplying by zero
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # Negative multiplication

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)      # Normal case
        self.assertEqual(self.calc.divide(5, 0), None)       # Division by zero
        self.assertEqual(self.calc.divide(-10, 2), -5.0)     # Negative result
        self.assertEqual(self.calc.divide(7, 3), 2.3333333333333335)  # Floating-point result

    def test_edge_cases(self):
        """Test edge cases."""
        self.assertEqual(self.calc.divide(0, 1), 0)          # Dividing zero by non-zero
        self.assertEqual(self.calc.divide(0, 0), None)       # Dividing zero by zero
        self.assertEqual(self.calc.add(1.1, 2.2), 3.3)      # Decimal numbers

if __name__ == "__main__":
    unittest.main()
