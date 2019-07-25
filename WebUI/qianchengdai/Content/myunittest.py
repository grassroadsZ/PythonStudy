"""
-*-conding: utf-8
@Time:2019-07-24 8:08
@Auther:grassroadsZ
@File:myunittest.py
"""
import unittest

from selenium import webdriver

from Content.handle_log import MyLog
from Pages.BidPage import Bid
from Pages.HomePage import Home
from Pages.LoginPage import Login


class MyUnittest(unittest.TestCase):
    logger = MyLog().logger

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.logger.info('初始化浏览器成功')
        cls.driver.implicitly_wait(10)
        cls.login = Login(cls.driver)
        cls.home = Home(cls.driver)
        cls.bid = Bid(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.logger.info('浏览器关闭')

