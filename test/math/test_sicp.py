from unittest import TestCase

import src.math.sicp as sicp


class TestSicp(TestCase):
    def test_f_iterative(self):
        actual = sicp.f_iterative(20)
        self.assertEqual(10771211, actual, 'test failed')
