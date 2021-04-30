import unittest
from calculator import Calculator


class TestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(5, 10), 15)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, 10), 50)

    def test_divide(self):
        self.assertAlmostEqual(self.calculator.divide(10, 5), 2)


if __name__ == "__main__":
    unittest.main()
