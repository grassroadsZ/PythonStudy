'''
-*-conding:utf-8
@Time:2019-05-21 19:00
@auther:grassroadsZ
@file:run.py.py
'''
import unittest
import time
import HTMLTestRunnerNew
from Homework.lesson_21_0520_fina_rewrite.test_two_division import TestDivision
from Homework.lesson_21_0520_fina_rewrite.test_add import TestAdd

load = unittest.TestLoader()
one_suite = (load.loadTestsFromTestCase( TestDivision ),load.loadTestsFromTestCase(TestAdd))
one_suite = unittest.TestSuite(tests = one_suite)
# load = unittest.TestSuite()
# one_suite = load.addTests(TestDivision().test_two_positive_division)
now = time.strftime( "%Y-%m-%d_%H-%M-%S" , time.localtime() )
fina = now + "_report"+ ".html"
with open( fina , "wb" ) as file:
    test_runner = HTMLTestRunnerNew.HTMLTestRunner( stream = file , verbosity = 2 , title = "测试报告" ,
                                                    description = "两数相加相除" , tester = "grassroadsZ" )
    test_runner.run( one_suite )