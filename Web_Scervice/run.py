'''
-*-conding:utf-8
@Time:2019-05-21 19:00
@auther:grassroadsZ
@file:run.py.py
'''
import unittest
import time
import os
from libs import HTMLTestRunnerNew
from options.File_path import REPORTS_PATH, CASES_PATH

one_load = unittest.TestLoader()
one_suite = unittest.TestLoader.discover(one_load, start_dir=CASES_PATH, pattern="test*.py" )

now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
fina = REPORTS_PATH
with open(os.path.join(fina, now + "_report" + ".html"), "wb") as file:
    test_runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title="测试报告",
        description="接口测试",
        tester="grassroadsZ")

    test_runner.run(one_suite)

