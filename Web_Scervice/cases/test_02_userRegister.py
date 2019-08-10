# -*-conding:utf-8
# @Time:2019-05-21 22:22
# @auther:grassroadsZ
# @file:test_01_SendCode.py

import unittest
import inspect
from json import loads
from libs.ddt import ddt, data
from options.handle_config import do_config
from options.handle_excel import ExcelOption
from options.handle_log import MyLog
from options import File_path
from options.handle_webservice import WebService
from options.handle_replace import DataReplace
from options.handle_mysql import HandleMysql


do_log = MyLog().out()


@ddt
class TestRegister(unittest.TestCase):
    """测试用户注册的类"""
    exl = ExcelOption(
        filename=File_path.Excel_File_Path,
        sheetname="userRegister")
    case_list = exl.get_cases()

    @classmethod
    def setUpClass(cls):
        do_log.info("{:*^40s}".format("测试注册开始"))
        cls.do_mysql = HandleMysql()
        cls.myrequest = WebService()

    @classmethod
    def tearDownClass(cls):
        do_log.info("{:*^40s}".format("测试注册结束"))
        cls.do_mysql.close()

    @data(*case_list)
    def test_userRegister(self, case_list):
        """
        测试注册
        :return: 当前测试用例的名称及测试结果
        """
        do_log.info("\n测试用例名称是{}".format(inspect.stack()[0][3]))
        case_num = case_list.case_id
        msg = case_list.tittle
        api = do_config("api", "base_url") + case_list.url
        method = case_list.apiname
        except_result = case_list.expected
        sql = case_list.sql
        data = DataReplace().phone_replace(case_list.data)
        res = TestRegister.myrequest(api, method, data)
        if sql and method == "sendMCode":
            mobile = loads(data).get("mobile")
            try:
                code = self.do_mysql(sql, args=mobile)["Fverify_code"]
            except TypeError:
                data = DataReplace().phone_replace(case_list.data)
                res = TestRegister.myrequest(api, method, data)
            DataReplace.code = code
            DataReplace.mobile = mobile

        try:
            self.assertEqual(loads(except_result), dict(res), msg=msg)
        except AssertionError as a:
            do_log.error("{}不通过,原因是{}\n".format(msg, a))
            self.exl.excel_write(
                row=case_num + 1,
                real_result=str(res),
                result=do_config(
                    "result",
                    "Fail"))
            raise a

        else:
            do_log.error("{},Pass\n".format(msg))
            self.exl.excel_write(
                row=case_num + 1,
                real_result=str(res),
                result=do_config(
                    "result",
                    "success"))


if __name__ == '__main__':
    unittest.main()
