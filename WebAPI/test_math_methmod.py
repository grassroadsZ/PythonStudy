'''
-*-conding:utf-8
@Time:2019/4/23 21:42
@auther:grassroadsZ
@file:test_math_methmod.py
'''

import unittest
from apibook.study_unit_test.mathtest import MathMethmod


class TestMathMethmod(unittest.TestCase):
    def test_two_positive(self):
        "两正数相加"
        MathMethmod(1,2).sub()

    def test_two_negative(self):
        "两负数相加"
        MathMethmod(-1,-2).sub()

    def test_two_positive_negative(self):
        "一正一负相加"
        MathMethmod(1,-2).sub()

    def test_zero_positive(self):
        "正数与0相加"
        MathMethmod(0,1).sub()

    def test_two_float(self):
        "浮点数相加"
        MathMethmod(0.1,0.2).sub()

if __name__ == '__main__':
    unittest.main()