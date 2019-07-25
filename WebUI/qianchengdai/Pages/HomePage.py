"""
-*-conding: utf-8
@Time:2019-07-24 7:45
@Auther:grassroadsZ
@File:HomePage.py
"""

from selenium.webdriver.common.by import By
from Content.base import BasePage


class Home(BasePage):
    """首页"""
    # 元素定位表达式
    invest_buttons = (By.XPATH, '//a[text()="抢投标"]')

    @property
    def invest_button(self):
        """抢投标按钮"""
        return self.find_elements(self.invest_buttons)[0]

    def click_invest_button(self):
        """点击抢投标"""
        self.logger.info('点击抢投标')
        return self.invest_button.click()