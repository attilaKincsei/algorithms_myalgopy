from unittest import TestCase, main
from parameterized import parameterized
from main.codewars_compilation.total_amount_of_points import points


class TestPoints(TestCase):
    def test_points1(self):
        self.assertEqual(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']), 10)

    def test_points2(self):
        self.assertEqual(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']), 30)

    def test_points3(self):
        self.assertEqual(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']), 0)

    def test_points4(self):
        self.assertEqual(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']), 15)

    def test_points5(self):
        self.assertEqual(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']), 12)
