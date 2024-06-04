from unittest import TestCase

import src.math.arithmetic.minmaxavg as mma


class TestMinMaxAvg(TestCase):
    def test_get_minimum(self):
        expected = -43
        actual = mma.get_minimum([-5, 23, 0, -9, 12, 99, 105, -43])
        self.assertEqual(expected, actual, 'Failed to get lowest value in list')

    def test_get_maximum(self):
        expected = 105
        actual = mma.get_maximum([-5, 23, 0, -9, 12, 99, 105, -43])
        self.assertEqual(expected, actual, 'Failed to get highest value in list')

    def test_get_average(self):
        expected = 22.75
        actual = mma.calculate_arithmetic_mean([-5, 23, 0, -9, 12, 99, 105, -43])
        self.assertEqual(expected, actual, 'Failed to get arithmetic mean of vector')

    def test_get_average_non_numeric(self):
        expected = 22.8
        actual = mma.calculate_arithmetic_mean([-5, 23, 0, "dupa", -9, 12, 99, [2, 44], None, 105, -43])
        self.assertEqual(expected, actual, 'Failed to get arithmetic mean of vector')
