"""
-*-conding: utf-8
@Time:2019-06-07 8:56
@Auther:grassroadsZ
@File:test_03_verifyUserAuth.py
"""

import unittest
from json import loads
from libs.ddt import ddt, data
from options import File_path
from options.handle_log import MyLog
from options.handle_config import HandleConfig
from options.handle_excel import ExcelOption
from options.handle_mysql import HandleMysql
from options.handle_webservice import WebService
from options.handle_replace import DataReplace


@ddt
class TestVerifyUserAuth( unittest.TestCase ):
    """测试实名认证的类"""
    exl = ExcelOption(filename=File_path.Excel_File_Path, sheetname="verifyUserAuth")
    case_list = exl.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.do_log = MyLog().out()
        cls.do_config = HandleConfig()
        cls.myrequest = WebService()
        cls.mysql = HandleMysql()
        cls.do_log.info("{:*^40s}".format("测试{}开始".format(cls.__doc__)))
        cls.mysql(sql="DELETE FROM user_db.t_user_auth_info where Ftrue_name in ('菜鸟');")

    @data(*case_list)
    def test_verifyUserAuth(self , case_list):
        """
        测试注册
        :return: 当前测试用例的名称及测试结果
        """
        # do_log.info("\n测试用例名称是{}".format(inspect.stack()[0][3]))
        case_num = case_list.case_id
        msg = case_list.tittle
        api = self.do_config( "api" , "base_url" ) + case_list.url
        method = case_list.apiname
        except_result = case_list.expected
        sql = case_list.sql
        data = DataReplace().phone_replace( case_list.data )
        res = TestVerifyUserAuth.myrequest(api, method, data)
        if sql and method == "sendMCode":
            mobile = loads(data).get( "mobile")
            try:
                code = self.mysql(sql, args=mobile)["Fverify_code"]
                if not code:
                    # 如果手机号有误或为None就从新请求
                    data = DataReplace().phone_replace(case_list.data)
                    res = TestVerifyUserAuth.myrequest(api, method, data)
            except TypeError:
                pass
            else:
                mobile = loads(data).get("mobile")
                code = self.mysql(sql, args=mobile)["Fverify_code"]
            DataReplace.code = code
            DataReplace.mobile = mobile

        if method == "userRegister" and "ok" in str(res):
            # 如果接口名是注册且返回是ok去数据库查uid
            uid = self.mysql(sql, loads(data)["user_id"])
            setattr(DataReplace, "uid", uid["Fuid"])

        try:
            self.assertEqual(loads(except_result), dict(res), msg=msg)
        except AssertionError as a:
            self.do_log.error("{}不通过,原因是{}\n".format(msg, a))
            self.exl.excel_write(row=case_num + 1,
                                 real_result=str(res),
                                 result=self.do_config("result", "Fail"))
            raise a

        else:
            self.do_log.error("{},Pass\n".format(msg))
            self.exl.excel_write(row=case_num + 1,
                                 real_result=str(res),
                                 result=self.do_config("result", "success"))

    @classmethod
    def tearDownClass(cls):
        cls.do_log.info("{:*^40s}".format("测试{}结束".format(cls.__doc__)))
        cls.mysql.close()


if __name__ == '__main__':
    unittest.main()
