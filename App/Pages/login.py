"""
-*-enconding: utf-8
@Time:2019-08-04 19:52
@Author:grassroadsZ
@File:login.py
Motto：good good study , day day up !!!
"""
import time

from selenium.webdriver.common.by import By

from Content.base import AppBase
from Datas.user_info import right_info


class Login(AppBase):
    """登陆页面"""

    # locator
    start = (By.ID, 'com.xxzb.fenwoo:id/btn_start')
    me = (By.XPATH, '//android.widget.TextView[@text=\"我\"]')
    phone = (By.ID, 'com.xxzb.fenwoo:id/et_phone')
    next_step = (By.ID, 'com.xxzb.fenwoo:id/btn_next_step')
    pwd = (By.ID, 'com.xxzb.fenwoo:id/et_pwd')

    def login(self):
        time.sleep(3)
        self.swipe_screen(num=3)
        self.click(self.start)
        self.click(self.me)
        self.input(self.phone, value=right_info['phone'])
        self.click(self.next_step)
        self.input(self.pwd, value=right_info['pwd'])
        self.click(self.next_step)


if __name__ == '__main__':
    login = Login()
    login.login()

