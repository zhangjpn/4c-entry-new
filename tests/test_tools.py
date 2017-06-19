# -*- coding:utf-8 -*-

import unittest
from app4c.tools import str_to_date, is_valid_vin, is_valid_license
import datetime
class ToolTestCase(unittest.TestCase):
    def setUp(self):
        self.vin = 'LDCT81X41E1171519'  # 'LDC633T26F3394106'
        self.license = '91310000088601758A'
        self.d = '   2017-11-23  23:  '
    @unittest.expectedFailure
    def test_str_to_date(self):
        d = str_to_date(self.d)
        print(d)
        self.assertIsInstance(d, datetime.datetime)

    def test_is_valid_vin(self):
        self.assertTrue(is_valid_vin(self.vin))


    def test_is_valid_license(self):
        self.assertTrue(is_valid_license(self.license))

    def tearDown(self):
        self.vin = None
        self.license = None


if __name__ == '__main__':
    unittest.main()