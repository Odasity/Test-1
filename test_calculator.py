import unittest

# Functions to test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test Cases
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, -8.0), 2.0)
        self.assertEqual(add(1, -1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(5, 10), 0.5)
        self.assertEqual(divide(9, 3), 3)
        
    def test_divide_by_zero(self):
        # Check if ValueError is raised
        with self.assertRaises(ValueError):
            divide(7, 0)

if __name__ == '__main__':
    unittest.main()



