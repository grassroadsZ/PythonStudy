'''
-*-conding:utf-8
@Time:2019-05-21 22:22
@auther:grassroadsZ
@file:test_add.py
'''
'''
-*-conding:utf-8
@Time:2019-05-21 6:53
@auther:grassroadsZ
@file:test_two_division.py
'''
import unittest,inspect,time
from Homework.lesson_21_0520_fina_rewrite.ddt  import ddt,data
from Homework.lesson_21_0520_fina_rewrite.handle_config import do_config
from Homework.lesson_21_0520_fina_rewrite.handle_excel import ExcelOption
from Homework.lesson_21_0520_fina_rewrite.handle_log import do_log
from Homework.lesson_21_0520_fina_rewrite.test_function import MathNum

@ddt
class TestAdd( unittest.TestCase ):
    """测试两数相加的类"""
    now = time.strftime( "%Y-%m-%d %H:%M:%S" , time.localtime() )
    exl = ExcelOption(filename = do_config("file path","excel_path"),sheetname = "add")
    case_list = exl.get_cases()


    @classmethod
    def setUpClass(cls):
        # cls.file_name = do_config("file path","report_path")
        # cls.file = open( cls.file_name , mode = "a" , encoding = "utf-8" )
        # cls.file.write( "{:*^40s}".format( "测试开始" ) )
        do_log.info("{:*^40s}".format( "测试开始" ))




    @classmethod
    def tearDownClass(cls):
        # cls.file.write( "{:*^40s}".format( "测试结束" ) )
        # cls.file.close()
        do_log.info( "{:*^40s}".format( "测试结束" ) )



    @data(*case_list)
    def test_two_positive_division(self,case_list):
        """
        两正数相除
        :return: 当前测试用例的名称及测试结果
        """

        result_address = "测试时间：{}测试用例名称是{},测试结果是： ".format( TestAdd.now , inspect.stack()[0][3] )

        msg = case_list.tittle
        except_result = case_list.except_result
        first_num = case_list.first_num
        second_num = case_list.second_num
        act_result = case_list.act_result
        case_num = case_list.case_num

        try:
            act_result = MathNum( first_num , second_num ).two_add()
            self.assertEqual( except_result , act_result , msg = msg )
        except AssertionError as a:
            # self.file.write("\n{}不通过,原因是{}\n".format(result_address,a))
            do_log.error("\n{}不通过,原因是{}\n".format(result_address,a))
            self.exl.excel_write( row = case_num + 1 , real_result = act_result , result = do_config("result","Fail") )
            raise a

        else:
            # self.file.write( "\n{},Pass\n".format(result_address + msg) )
            do_log.error( "\n{},Pass\n".format(result_address + msg) )
            self.exl.excel_write( row = case_num+1 , real_result = act_result , result =do_config("result","success") )