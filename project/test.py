from fractions import Fraction
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()

# Results show an ImportError stating the program cannot import 'sum' from 'my_sum' since it believes that the searched file is missing. Interestingly enough, there is a lack of an error on the fractions as the AssertionError is not present. After looking at the code, I couldn't find anything for why this event was happening. Perhaps there's an installation error that happened during the test that could've affected the program.
