"""
-*-conding: utf-8
@Time:2019-07-25 21:19
@Auther:grassroadsZ
@File:run.py
"""


import time
import unittest
from Content.File_path import REPORTS_PATH, CASES_PATH
from Content.handle_log import MyLog
from libs.HTMLTestRunner_cn import HTMLTestRunner


def cases_suite():
    """测试套件"""
    oneload = unittest.TestLoader()
    suite = unittest.TestLoader.discover(oneload, start_dir=CASES_PATH, pattern='test_*.py')
    return suite


def main():
    now_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    report_path = REPORTS_PATH + '/' + now_time + "_report" + ".html"
    try:
        with open(report_path, 'wb') as f:
            runner = HTMLTestRunner(stream=f,
                                    description='前程贷UI自动化测试',
                                    title='Ui自动化测试报告',
                                    tester='grassroadsZ',
                                    verbosity=2)
            runner.run(cases_suite())
    except Exception as e:
        MyLog().logger.error("执行测试套件错误{}".format(e))
    else:
        MyLog().logger.info("所用用例执行完成, 并生成测试报告:{}".format(report_path))


if __name__ == '__main__':
    main()


