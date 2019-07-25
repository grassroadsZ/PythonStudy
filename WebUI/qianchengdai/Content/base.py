"""
-*-conding: utf-8
@Time:2019-07-18 15:36
@Auther:grassroadsZ
@File:base.py
"""

import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from Content.File_path import IMG_PATH
from Content.handle_log import MyLog


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.logger = MyLog().logger

    def wait_element(self, locator):
        wait = WebDriverWait(self.driver, self.timeout)
        return wait.until(Ec.element_to_be_clickable(locator))

    def visit_url(self, url):
        return self.driver.get(url)

    def click(self, locator):
        try:
            ele = self.find_element(locator)
            ele.click()
        except (NoSuchElementException, TimeoutError)as e:
            self.logger.error(e + "{}".format('元素不可点击'))
            raise e

    def find_element(self, locator) -> WebElement:
        """获取一个元素对象"""
        wait = WebDriverWait(driver=self.driver, timeout=self.timeout)
        try:
            ele = wait.until(Ec.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"获取元素对象失败，失败原因为{e}")
            raise e
        else:
            return ele

    def find_elements(self, locator) -> list:
        """获取一个元素对象"""
        wait = WebDriverWait(driver=self.driver, timeout=self.timeout)
        try:
            ele = wait.until(Ec.presence_of_all_elements_located(locator))
        except (TimeoutError, NoSuchElementException) as e:
            self.logger.error(f"获取一组元素对象失败，失败原因为{e}")
            raise e
        else:
            return ele

    def send_keys(self, location, value) -> None:
        """
        input the value to input box of element
        :param location: //*[@by="location"]
        :param value: 输入的数据
        :return: None
        """
        try:
            element = self.find_element(location)
            element.clear()
            element.send_keys(value)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error("输入框:{}, 输入数据{}失败:{}".format(location, value, e))
            self.save_screen_shot("send_keys")
            raise e

    def get_element_text(self, locator):
        ele = self.find_element(locator)
        try:
            value = ele.text
        except AttributeError:
            value = ele.get_attribute('value')
            self.logger.error('获取元素对象文本失败')
        return value

    def save_screen_shot(self, info: str = ''):
        """
        屏幕截图
        :param info:
        :return:
        """
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        filename = IMG_PATH + '/' + current_time + info + '.png'
        return self.driver.save_screenshot(filename)


if __name__ == '__main__':
    pass
