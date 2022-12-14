import unittest
from prime import is_prime

# A class containing all of our tests
class Test(unittest.TestCase):
    def test_1(self):
        """Check that 1 is not prime"""
        self.assertFalse(is_prime(1))
    def test_2(self):
        self.assertFalse(is_prime(2))
    def test_8(self):
        self.assertFalse(is_prime(8))
    def test_11(self):
        self.assertFalse(is_prime(11))
    def test_25(self):
        self.assertFalse(is_prime(25))
    def test_28(self):
        self.assertFalse(is_prime(28))

# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()