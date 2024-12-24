#import unittest
import pytest

# Functions to test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test Cases
#class TestCalculator(unittest.TestCase):
#    def test_add(self):
#        self.assertEqual(add(10, -8.0), 2.0)
#        self.assertEqual(add(1, -1), 0)
#        self.assertEqual(add(0, 0), 0)

#    def test_divide(self):
#        self.assertEqual(divide(5, 10), 0.5)
#        self.assertEqual(divide(9, 3), 3)
        
#    def test_divide_by_zero(self):
#        # Check if ValueError is raised
#        with self.assertRaises(ValueError):
#            divide(7, 0)
#class TestCalculator():
@pytest.fixture
def sample_data():
    return {"a": [5, 9, 7], "b": [10, 3, 0]}

@pytest.mark.parametrize("a, b, expected", [(10, -8.0, 2.0), (1, -1, 0), (-2, -5, -7)])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_divide(sample_data):
    assert divide(sample_data["a"][0], sample_data["b"][0]) == 0.5
    assert divide(sample_data["a"][1], sample_data["b"][1]) == 3

def test_divide_by_zero(sample_data):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(sample_data["a"][2], sample_data["b"][2])


if __name__ == '__main__':
    pytest.main()
#    unittest.main()



