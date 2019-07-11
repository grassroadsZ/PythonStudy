'''
-*-conding:utf-8
@Time:2019/5/1 22:31
@auther:grassroadsZ
@file:lesson_15_0429.py
'''


 # 一、必做题
# 1.使用测试套件批量执行用例的顺序是？
# 先使用Unittest.TestSuite() 生成测试套件
# 再加载测试对象或测试类或测试模块，或是在创建测试套件时就加载模块
# 执行测试用例

# 2.将用例加载到测试套件中，有哪几种方式？
# 通过测试对象进行加载
# obj = unittest.TestSuite()
# obj.addTest(class("fun_name"))
# 通过测试类进行加载
# obj = unittest.TestLoader()
# obj.addTest(obj.loadTestsFromTestCase(class_name))
# 通过模块批量加载
# obj = unittest.TestLoader()
# obj.addTest(obj.loadTestsFromModule(module_name))

# 创建测试套件时就加载测试用例(用的最多)
# obj = unittest.TestLoader()
# test_module_tuple = (obj.loadTestsFromModule(module_name),obj.loadTestsFromModule(module_name))
# obj_suite = unittest.TestSuite(test_module_tuple)


# 3.编写如下单元测试 将上一次作业中的两数相减测试类与两数相除测试类的所有用例，使用测试套件来批量执行，然后将执行结果生成报表。
import unittest
import HTMLTestRunnerNew
from Homework import lesson_14_0426 as test1

# 创建测试套件
one_load = unittest.TestLoader()
test_module_tuple = (one_load.loadTestsFromModule(test1),)

# 加载模块
one_suite = unittest.TestSuite(test_module_tuple)

# 执行测试用例
with open("report.html","wb") as file:
    test_runner = HTMLTestRunnerNew.HTMLTestRunner(stream = file,verbosity = 2,title = "测试报告",
                                                   description = "两数相加相除",tester = "grassroadsZ")
    test_runner.run(one_suite)



