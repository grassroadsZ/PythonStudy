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
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait


class AppBase:
    """App测试基础类"""

    def __init__(self, parms):
        """初始化一个会话对象"""
        # self.driver = driver
        self.driver = webdriver.Remote(parms)
        self.driver.implicitly_wait(10)

    def find_element(self, by_locator: tuple, timeout=5):
        """查找定位元素"""
        wait = WebDriverWait(self.driver, timeout)
        try:
            ele = wait.until(Ec.presence_of_element_located(*by_locator))
        except Exception as e:
            msg = f"{by_locator}出现异常，元素未找到，异常为{e}"
            raise msg
        return ele

    @property
    def get_screen_size(self):
        widht = self.driver.get_window_size()['width']
        hight = self.driver.get_window_size()['height']
        widht = widht * 0.85
        hight = hight * 0.85
        return widht, hight

    def swipe_screen(self, direction='left', num=1, timeout=0.5):
        """
        屏幕滑动,默认左滑
        :param direction: 滑动的方向，默认为左滑,left/right/top/down
        :param num: 滑动次数
        :param timeout: 滑动后等待时间
        :return:
        """
        direction = direction.lower()
        widht, hight = self.get_screen_size

        if direction == 'left':
            for _ in range(num):
                self.driver.swipe(*self.get_screen_size, 0, hight)
                time.sleep(timeout)

        elif direction == 'right':
            for _ in range(num):
                self.driver.swipe(0, hight, *self.get_screen_size)
                time.sleep(timeout)

        elif direction == 'top':
            for _ in range(num):
                self.driver.swipe(*self.get_screen_size, widht, 0)
                time.sleep(timeout)

        elif direction == 'down':
            for _ in range(num):
                self.driver.swipe(widht, 0, *self.get_screen_size)
                time.sleep(timeout)
        else:
            msg = "输入有误，不支持的滑动方式"
            raise msg


