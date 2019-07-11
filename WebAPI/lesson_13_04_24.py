'''
-*-conding:utf-8
@Time:2019/4/25 21:53
@auther:grassroadsZ
@file:lesson_13_04_24.py
'''

# 一、必做题
# 1.什么是自动化测试？
# 自动化测试是指在业务流程变动较小的前提下，对于接口，UI等通过代码的方式对于不会有过多的变动所做的一种测试方式，自动化测试是建立在业务基础之上的。只有熟悉业务，理解需求才能做好自动化测试。

# 2.自动化测试的流程？
# 分析需求，编写自动化测试用例，搭建自动化测试框架，编写自动化测试脚本，脚本执行，生成结果报告

# 3.doctest如何使用？
# doctest用于函数定义的下方使用 >>> 第一行是测试用例，第二行是预期结果

# 4.单元测试的作用？
# 验证代码的行为与预期结果是否一致，对于代码有所改动时不需要再次重复对代码进行测试代码的编写

# 5.unittest框架中，如何测试多条用例？用例执行顺序？
# unittest中执行多条测试用例可以使用unittest.main()入口函数的方法，TestCase类会自动运行以test_开头的测试用例，用例执行的顺序以ASCII码的顺序执行，从大到小

'''
# 6.编写如下单元测试
# 使用unittest框架来测试两数相减功能，编写用例，执行用例。

class MathMethmod:
    "两数相减"
    def __init__(self,a, b):
        self.a, self.b = a, b

    def sub(self):
        return  self.a - self.b

import unittest
import inspect
class TestMathMethmod(unittest.TestCase):
    "对两数相减的测试类"
    def test_two_positive(self):
        print("当前执行的测试用例是{}".format(inspect.stack()[0][3]))
        "两正数相减"
        result = MathMethmod(1,2).sub()
        if result == -1:
            print("pass")
        else:
            print("fail")

    def test_two_negative(self):
        "两负数相加"
        print("当前执行的测试用例是{}".format(inspect.stack()[0][3]))
        result = MathMethmod(-1,-2).sub()
        if result == 1:
            print( "pass" )
        else:
            print( "fail" )

    def test_two_positive_negative(self):
        print("当前执行的测试用例是{}".format(inspect.stack()[0][3]))
        "一正一负相减"
        result = MathMethmod(1,-2).sub()
        if result == 3:
            print( "pass" )
        else:
            print( "fail" )

    def test_zero_positive(self):
        print("当前执行的测试用例是{}".format(inspect.stack()[0][3]))
        "正数与0相减"
        result = MathMethmod(0,1).sub()
        if result == -1:
            print( "pass" )
        else:
            print( "fail" )

    def test_two_float(self):
        print("当前执行的测试用例是{}".format(inspect.stack()[0][3]))
        "浮点数相加"
        result = MathMethmod(0.1,0.2).sub()
        if result == -0.1:
            print( "pass" )
        else:
            print( "fail" )

if __name__ == '__main__':
    unittest.main()
'''
# 二、选作题
# 7.编写如下单元测试
# a.使用unittest框架来测试两数相除功能，编写用例，执行用例。
# b.使用文件来记录执行用例的结果
'''
实现思路，定义两个类，一个类是测试用例类，一个是文件操作类，然后再定义一个类继承这两个类，通过这个继承了两个类的类完成所有测试及写入操作
问题：当测试类中捕获异常后，测试会被通过，不是fail，因此无法记录失败了几个，全部都是pass，当重新抛出异常后失去了捕获的意义，对于单元测试中的方法掌握不熟练，前面知识综合后运用不到位。
'''



class MathDivision():

    def __init__(self,a ,b):
        self.a ,self.b = a, b

    def two_division(self):
        return self.a / self.b

import unittest
import inspect
import time

class TestDivision(unittest.TestCase):
    """测试两数相除的类"""
    now = time.strftime( "%Y-%m-%d %H:%M:%S" , time.localtime() )
    @classmethod
    def setUpClass(cls):
        cls.file_name = "test_result.txt"
        cls.file = open(cls.file_name, mode = "a", encoding = "utf-8")
        cls.file.write("{:*^40s}".format("测试开始"))

    def test_two_positive_division(self):
        """
        两正数相除
        :return: 当前测试用例的名称及测试结果
        """
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format(TestDivision.now,inspect.stack()[0][3])
        except_result = 0.5
        msg = "测试两正数相除"
        try:
            result = MathDivision(5,10).two_division()
            self.assertEqual( except_result , result , msg = msg )
        except AssertionError as a:
            self.file.write("\n{}不通过,原因是{}\n".format(result_address,a))
        else:
            self.file.write( "\n{},Pass\n".format(result_address + msg) )

    def test_two_negative(self):
        """
        两负数相除
        :return: 当前测试用例的名称及测试结果
        """
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        except_result = 0.5
        msg = "测试两正数相除"
        try:
            result = MathDivision(-5,-10).two_division()
            self.assertEqual( except_result , result , msg = msg )
        except AssertionError as a:
            self.file.write("\n{}不通过,原因是{}\n".format(msg,a))
        else:
            self.file.write( "\n{},Pass\n".format(result_address + msg) )

    def test_positive_negative(self):
        """
        一正数一负数相除
        :return: 当前测试用例的名称及测试结果
        """
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        except_result = -0.5
        msg = "测试一正一负相除"
        try:
            result = MathDivision( 5 , -10 ).two_division()
            self.assertEqual(except_result,result,msg=msg)
        except AssertionError as a:
            self.file.write("\n{}不通过,原因是{}\n".format(msg,a))
        else:
            self.file.write( "\n{},Pass\n".format(result_address + msg) )


    def test_num_str(self):
        """
        一数与字符串相除
        :return: 当前测试用例的名称及测试结果
        """
        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestDivision.now , inspect.stack()[0][3] )
        # msg = "测试数字与字符串相除"
        try:
            result = MathDivision( 5 , 'r' ).two_division()
        except TypeError as a:
            self.file.write( "\n{}不通过,原因是{}\n".format( result_address , a ))
            raise a

    @classmethod
    def tearDownClass(cls):
        cls.file.write( "{:*^40s}".format( "测试结束" ) )
        cls.file.close()

if __name__ == '__main__':
    unittest.main()
