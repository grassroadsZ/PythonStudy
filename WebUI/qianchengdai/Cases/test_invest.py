"""
-*-conding: utf-8
@Time:2019-07-24 7:55
@Auther:grassroadsZ
@File:test_invest.py
"""
import inspect

from ddt import ddt, data

from Content.myunittest import MyUnittest
from Datas import login_data, invest_data


@ddt
class TestInvest(MyUnittest):
    success_data = login_data.login_success_data[0]
    invest_suc_data = invest_data.invest_success

    def setUp(self):
        self.login.login(self.success_data['user'], self.success_data['pwd'])
        self.home.click_invest_button()

    @data(*invest_suc_data)
    def test_invest(self, invest_data):
        self.bid.input_money(invest_data['amount'])
        actual = self.bid.get_invest_success_info
        self.logger.info(f'投标实际结果{actual}')
        try:
            self.assertEqual(invest_data['expect'], actual)
        except AssertionError as e:
            self.logger.error(f"断言{inspect.stack()[0][3]}失败,原因：{e}")
            self.home.save_screen_shot(inspect.stack()[0][3]+'_fail')
