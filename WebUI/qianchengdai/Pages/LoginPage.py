"""
-*-conding: utf-8
@Time:2019-07-22 7:40
@Auther:grassroadsZ
@File:LoginPage.py
"""
from pygments.formatters import img
from selenium.webdriver.common.by import By

from Content.base import BasePage


class Login(BasePage):
    """登陆页面"""

    # 元素定位表达式
    phone_input = (By.XPATH, '//input[@name = "phone"')
    password_input = (By.XPATH, '//input[@name = "password"')
    v_code = (By.XPATH, '//input[@name = "vcode"')
    v_code_img = (By.XPATH, '//img[@class ="verify-img"')
    login_button = (By.XPATH, '//button[text()="登录"')
    format_error_info = (By.XPATH, '//div[@class ="form-error-info"')
    phone_password_error = (By.XPATH, '//div[@class ="layui-layer-content"')
    login_success_info = (By.XPATH, '//a[text()="我的帐户[python10]"')

    def login(self, phone: str, password: str):
        self.input_user(phone)
        self.input_password(password)
        self.click_login()

    def input_user(self, phone):
        self.send_keys(location=self.phone_input, value=phone)

    def input_password(self, password):
        self.send_keys(location=self.password_input, value=password)

    def click_login(self):
        self.click(self.login_button)

    @property
    def get_login_success_info(self):
        value = self.get_element_text(*self.login_success_info)
        return value
