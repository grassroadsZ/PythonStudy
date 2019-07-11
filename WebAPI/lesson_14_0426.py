'''
-*-conding:utf-8
@Time:2019/4/27 14:00
@auther:grassroadsZ
@file:lesson_14_0426.py
'''

# 1.查看第一次作业中自己定的小目标，现在达成了多少？是否还在坚持？是否想退缩了？
# 目标算是达成了一点点，有一点点工程思维了，搭建接口自动化测试框架的话还远远不够，路还很遥远，庆幸的是每天还是有一点点的进步的

# 2.unittest中有哪几种用例执行前后的处理方式？它们之间有什么区别？
'''
def setUp(self):
# 每一个用例执行前都会被执行，多用于单个函数的测试用例
def tearDown(self)
# 每个用例执行结束后都会执行

@classmethmod
def setUpClass(cls):
# 所有测试用例执行前都会被调用一次，多用于测试一个类
@classmethmod
def tearDownClass(cls):
# 所有测试用例执行结束后都会被调用一次    

def setUpModule():
    # 所有测试类被调用前执行一次，多用于多个测试类
    与glboal全局变量配合使用
def tearDownModule():
# 所有测试类被调用结束后执行一次，多用于多个测试类

unittest.skip( 'test_pass测试用例会被跳过' )
def test_pass():
'''


import unittest
import inspect
import time

class MathNum:
    def __init__(self,a ,b):
        self.a ,self.b = a, b

    def two_division(self):
        return self.a / self.b

    def two_sub(self):
        return self.a - self.b

def setUpModule():
    file_name = "test_module_result.txt"
    global file
    file = open( file_name , mode = "a" , encoding = "utf-8" )
    file.write( "{:*^80s}".format( "测试用例开始执行" ) )

def tearDownModule():
    file.write( "{:*^80s}".format( "测试用例执行结束" ) )
    file.write("\n"* 2)
    file.close()

class TestDivision( unittest.TestCase ):
    """测试两数相除的类"""
    now = time.strftime( "%Y-%m-%d %H:%M:%S" , time.localtime() )
    def test_two_positive_division(self):
        """
        两正数相除
        :return: 当前测试用例的名称及测试结果
        """
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        except_result = 0.5
        msg = "测试两正数相除"
        try:
            result = MathNum( 5 , 10 ).two_division()
            self.assertEqual( except_result , result , msg = msg )
        except AssertionError as a:
            file.write("\n{}不通过,原因是{}\n".format(result_address,a))
        else:
            file.write( "\n{},Pass\n".format(result_address + msg) )
            self.assertAlmostEqual()

    def test_two_negative(self):
        """
        两负数相除
        :return: 当前测试用例的名称及测试结果
        """
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        except_result = 0.5
        msg = "测试两正数相除"
        try:
            result = MathNum( -5 , -10 ).two_division()
            self.assertEqual( except_result , result , msg = msg )
        except AssertionError as a:
            file.write("\n{}不通过,原因是{}\n".format(msg,a))
        else:
            file.write( "\n{},Pass\n".format(result_address + msg) )

    def test_positive_negative(self):
        """
        一正数一负数相除
        :return: 当前测试用例的名称及测试结果
        """
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        except_result = -0.5
        msg = "测试一正一负相除"
        try:
            result = MathNum( 5 , -10 ).two_division()
            self.assertEqual(except_result,result,msg=msg)
        except AssertionError as a:
            file.write("\n{}不通过,原因是{}\n".format(msg,a))
        else:
            file.write( "\n{},Pass\n".format(result_address + msg) )


    def test_num_str(self):
        """
        一数与字符串相除
        :return: 当前测试用例的名称及测试结果
        """
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        # msg = "测试数字与字符串相除"
        try:
            MathNum( 5 , 'r' ).two_division()
        except TypeError as a:
            file.write( "\n{}不通过,原因是{}\n".format( result_address , a ))
            raise a



class TestMathSub( unittest.TestCase ):
    "对两数相减的测试类"
    def test_two_positive(self):
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        except_result = -5
        msg = "测试两正数相减"
        try:
            result = MathNum( 5 , 10 ).two_sub()
            self.assertEqual( except_result , result , msg = msg )
        except AssertionError as a:
            file.write("\n{}不通过,原因是{}\n".format(result_address,a))
        else:
            file.write( "\n{},Pass\n".format(result_address + msg) )


    def test_two_negative(self):
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        except_result = 1
        msg = "两负数相减"
        try:
            result = MathNum( -1 , -2 ).two_sub()
            self.assertEqual( except_result , result , msg = msg )
        except AssertionError as a:
            file.write("\n{}不通过,原因是{}\n".format(result_address,a))
        else:
            file.write( "\n{},Pass\n".format(result_address + msg) )

    def test_two_positive_negative(self):
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        except_result = 1
        msg = "一正一负相减"
        try:
            result = MathNum( 1 , -2 ).two_sub()
            self.assertEqual( except_result , result , msg = msg )
        except AssertionError as a:
            file.write( "\n{}不通过,原因是{}\n".format( result_address , a ) )
        else:
            file.write( "\n{},Pass\n".format( result_address + msg ) )

    def test_zero_positive(self):
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        msg = "正数与0相减"
        except_result = 1
        try:
            result = MathNum( 1 , 0 ).two_sub()
            self.assertEqual( except_result , result , msg = msg )
        except AssertionError as a:
            file.write( "\n{}不通过,原因是{}\n".format( result_address , a ) )
        else:
            file.write( "\n{},Pass\n".format( result_address + msg ) )


    def test_two_float(self):
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        msg = "浮点数相减"
        except_result = -0.1
        try:
            result = MathNum( 0.1 , 0.2 ).two_sub()
            self.assertEqual( except_result , result , msg = msg )
        except AssertionError as a:
            file.write( "\n{}不通过,原因是{}\n".format(result_address, a ))
        else:
            file.write( "\n{},Pass\n".format(result_address + msg))

if __name__ == '__main__':
    unittest.main()
