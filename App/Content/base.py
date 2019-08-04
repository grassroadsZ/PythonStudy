"""
-*-enconding: utf-8
@Time:2019-08-02 7:45
@Author:grassroadsZ
@File:base.py
Motto：good good study , day day up !!!
"""

# App测试基础文件类
import time

from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait

from Config.app_params import parms, ip_port


class AppBase:
    """App测试基础类"""

    def __init__(self):
        """初始化一个会话对象"""
        # self.driver = driver
        self.driver = webdriver.Remote(ip_port, desired_capabilities=parms)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, timeout=5)

    def find_element(self, by_locator: tuple) ->WebElement:
        """查找定位元素"""
        try:
            ele = self.wait.until(Ec.presence_of_element_located(by_locator))
        except Exception as e:
            msg = f"{by_locator}出现异常，元素未找到，异常为{e}"
            raise msg
        return ele

    def swipe_screen(self, direction='left', num=1, timeout=1.5):
        """
        屏幕滑动,默认左滑
        :param direction: 滑动的方向，默认为左滑,left/right/top/down
        :param num: 滑动次数
        :param timeout: 滑动后等待时间
        :return:
        """
        direction = direction.lower()
        widht_start, hight_start, widht_end, hight_end = self.get_screen_size

        if direction == 'left':
            for _ in range(num):
                self.driver.swipe(widht_end, hight_start, widht_start, hight_start)
                time.sleep(timeout)

        elif direction == 'right':
            for _ in range(num):
                self.driver.swipe(widht_start, hight_start, widht_end, hight_start)
                time.sleep(timeout)

        elif direction == 'top':
            for _ in range(num):
                self.driver.swipe(widht_end, hight_end, widht_start, hight_start)
                time.sleep(timeout)

        elif direction == 'down':
            for _ in range(num):
                self.driver.swipe(widht_end, hight_start, widht_start, hight_end)
                time.sleep(timeout)
        else:
            msg = "输入有误，不支持的滑动方式"
            raise msg

    def input(self, locator, value):
        """输入"""
        return self.find_element(locator).send_keys(value)

    def click(self, by_locator):
        """点击"""
        try:
            ele = self.wait.until(Ec.element_to_be_clickable(by_locator))
        except Exception as a:
            msg = f"{by_locator}是否有问题，元素并不能点击！错误为{a}"
            raise msg
        return ele.click()

    @property
    def get_screen_size(self):
        widht = self.driver.get_window_size()['width']
        hight = self.driver.get_window_size()['height']
        widht_end = widht * 0.85
        widht_start = widht * 0.3
        hight_end = hight * 0.8
        hight_start = hight * 0.3
        return widht_start, hight_start, widht_end, hight_end






