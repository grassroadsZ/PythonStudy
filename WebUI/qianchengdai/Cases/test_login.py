"""
-*-conding: utf-8
@Time:2019-07-22 7:39
@Auther:grassroadsZ
@File:test_login.py
"""

import unittest
from webbrowser import Chrome
from ddt import ddt, data

from Content.base import BasePage
from Datas import login_data
from Pages.LoginPage import Login


@ddt
class TestLogin(unittest.TestCase):
    success_data = login_data.login_success_data

    def setUp(self):
        self.driver = Chrome()
        self.login = Login(self.driver)

    @data(*success_data)
    def test_login_success(self, success):
        # print(success['user'])
        self.login.login(success['user'], success['pwd'])
        actul = self.login.get_login_success_info
        self.assertEqual(self.login.login_success_info, actul)

