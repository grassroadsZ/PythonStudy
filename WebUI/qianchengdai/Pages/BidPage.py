"""
-*-conding: utf-8
@Time:2019-07-25 7:27
@Auther:grassroadsZ
@File:BidPage.py
"""
from selenium.webdriver.common.by import By

from Content.base import BasePage


class Bid(BasePage):
    """投资页面"""

    # 元素定位表达式
    amount_money = (By.XPATH, "//div[contains(@class,'clearfix')]/input")
    invest_button = (By.XPATH, '//button[contains(@class, "btn-special")]')
    invest_success = (By.XPATH, "//div[@class='layui-layer-content']//div[contains(@class,'capital_font1')]")

    def input_money(self, money):
        self.logger.info(f'输入投资金额{money}')
        return self.send_keys(self.amount_money, value=money)

    def click_invest_button(self):
        self.logger.info('点击投标按钮')
        return self.click(self.invest_button)

    @property
    def user_money(self):
        """账户余额"""
        return self.find_element(self.amount_money).get_attribute('data-amount')

    @property
    def get_invest_success_info(self):
        return self.get_element_text(self.invest_success)
