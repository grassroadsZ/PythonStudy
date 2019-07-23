"""
-*-conding: utf-8
@Time:2019-07-22 7:40
@Auther:grassroadsZ
@File:LoginPage.py
"""

from selenium.webdriver.common.by import By
from Content.base import BasePage


class Login(BasePage):
    """登陆页面"""

    # 元素定位表达式
    phone_input = (By.NAME, "phone")
    password_input = (By.NAME, "password")
    v_code = (By.NAME, "vcode")
    v_code_img = (By.XPATH, '//img[@class="verify-img"')
    login_button = (By.XPATH, "//button[@class='btn btn-special']")
    format_error_info = (By.XPATH, '//div[@class="form-error-info"')
    phone_password_error = (By.XPATH, '//div[@class="layui-layer-content"')
    login_success_info = (By.XPATH, "//a[contains(text(),'[python10]')]")
    url = 'http://120.78.128.25:8765/Index/login.html'

    def login(self, phone: str, password: str):
        self.visit_url(self.url)
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
        value = self.get_element_text(self.login_success_info)
        return value

if __name__ == '__main__':
    pass