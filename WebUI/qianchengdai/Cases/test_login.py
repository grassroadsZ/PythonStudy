"""
-*-conding: utf-8
@Time:2019-07-22 7:39
@Auther:grassroadsZ
@File:test_login.py
"""

import inspect
from ddt import ddt, data
from Content.myunittest import MyUnittest
from Datas import login_data


@ddt
class TestLogin(MyUnittest):
    """测试登陆的类"""
    # 测试数据，从py文件内获取
    success_data = login_data.login_success_data

    def setUp(self):
        self.logger.info('刷新当前页面')
        self.driver.refresh()

    @data(*success_data)
    def test_login_success(self, success):
        self.login.login(success['user'], success['pwd'])
        actual = self.login.get_login_success_info
        self.logger.info(f"实际结果为：{actual}")
        try:
            self.assertEqual(success['expect'], actual)
        except AssertionError as e:
            self.logger.error(f"测试{inspect.stack()[0][3]}失败, 原因：{e})")
            self.login.save_screen_shot(inspect.stack()[0][3]+'_fail')


