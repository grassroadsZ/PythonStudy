"""
-*-conding: utf-8
@Time:2019-07-22 7:39
@Auther:grassroadsZ
@File:test_login.py
"""

import unittest
from ddt import ddt, data
from selenium import webdriver
from Datas import login_data
from Pages.LoginPage import Login


@ddt
class TestLogin(unittest.TestCase):
    success_data = login_data.login_success_data

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login = Login(self.driver)

    @data(*success_data)
    def test_login_success(self, success):
        self.login.login(success['user'], success['pwd'])
        actual = self.login.get_login_success_info
        self.assertEqual(success['expect'], actual)

