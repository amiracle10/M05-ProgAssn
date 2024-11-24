import unittest
from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of Integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1,4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, Fraction(9, 10))


if __name__ =='__main__':
    unittest.main()
    

# test results explanation

# I created two test cases to validate the functionality of the my_sum function:

# 1. test_list_int checks if the function can sum a list of integers. The input was 
# [1, 2, 3] and the function returned 6 which matched the expected result. This indicates
# the function handles integer inputs correctly

# 2. test_list_fraction verifies if the function can sum a lis of fractions. The input
# was [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)] and the function returned
# Fraction(9, 10). The test failed because the expected value is incorrectly set to 1.
# If you update the expected value to Fraction(9,10), it will pass.

# The test results show that my_sum function is working as expected for summing a list
# of integers. The test case for integer inputs passed because the function correctly
# returned the sum of the lsit. However, the test summing fractions failed. This does not
# indicate a problem with the my_sum function itself. the test failed because expected 
# result was incorrectly set to 1 instead of Fraction(9, 10). this means the function
# is capable of handling fractions correctly, but the test case needs to be updated 
# to reflect the correct expected outcome. 