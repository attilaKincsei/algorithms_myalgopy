from unittest import TestCase
from parameterized import parameterized

import src.math.arithmetic.divisibility as mad


class TestDivisibility(TestCase):

    # @parameterized.expand([0, 1, 4, 9, 10, 100])
    # def test_check_if_prime_fermat__false(self, integer):
    #     self.assertFalse(mad.check_if_prime_fermat(integer), f"Integer is not prime: {integer}")
    #
    @parameterized.expand([2, 3, 7, 11, 13, 17, 19, 9973])
    def test_check_if_prime_fermat__true(self, integer):
        self.assertTrue(mad.check_if_prime_fermat(integer), f"Integer is prime: {integer}")

    @parameterized.expand(
            [
                [43, 43],
                [44, 2],
                [9973, 9973],
             ]
    )
    def test_smallest_divisor(self, number, expected):
        actual = mad.smallest_divisor(number)
        self.assertEqual(expected, actual, f"Not the smallest divisor: {actual}")
