#day2 chapGPT's 10 day automation preparation course
#unittest exercise

import unittest

class TestMathOperations(unittest.TestCase):
    def setUp(self):
        print("Setting up resources")
        
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_multiplication(self):
        self.assertNotEqual(2 * 3, 5)
        self.assertIn('apple', ['apple', 'banana'])

    def tearDown(self):
        print("Cleaning up resources")


if __name__ == '__main__':
    unittest.main()