from unittest import TestCase
from parameterized import parameterized

import src.arraystring.trapping_rainwater as trw


class TestTrapRW(TestCase):

    @parameterized.expand(
            [
                [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
                [[4, 2, 0, 3, 2, 5], 9],
                [[2, 0, 2], 2],
                [[4, 2, 3], 1],
            ]
    )
    def test_trap(self, nums, expected):
        self.maxDiff = None
        actual = trw.trap(nums)
        self.assertEqual(expected, actual)
