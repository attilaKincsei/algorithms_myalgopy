from unittest import TestCase
from parameterized import parameterized

import src.search.bfs as bfs


class TestBfs(TestCase):

    @parameterized.expand(
            [
                [[2, 3, 1, 1, 4], 2],
                [[2, 3, 1, 1, 4], 2],
                [[6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8], 2],
            ]
    )
    def test_jump(self, nums, expected):
        actual = bfs.jump(nums)
        self.assertEqual(expected, actual)

