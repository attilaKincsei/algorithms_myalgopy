from unittest import TestCase

import src.devops.loyal_customer as lc


class TestLoyalCustomer(TestCase):
    file_path_1 = "/home/iguana/akde/PRACTICE/ALGORITHMS/myalgo_py/test/resources/loyal_customer_1.log"
    file_path_2 = "/home/iguana/akde/PRACTICE/ALGORITHMS/myalgo_py/test/resources/loyal_customer_2.log"

    @classmethod
    def setUpClass(cls):
        cls.customer_dict_1 = lc.read_csv_as_customer_dict(cls.file_path_1)
        cls.customer_dict_2 = lc.read_csv_as_customer_dict(cls.file_path_2)

    def test_find_loyal_customer(self):
        expected = ['488', '793', '1202']
        actual = lc.find_loyal_customer(2, self.customer_dict_1, self.customer_dict_2)
        self.assertEqual(expected, actual, 'Failed to identify loyal customers as per specification')
