"""
-*-conding: utf-8
@Time:2019-07-18 15:36
@Auther:grassroadsZ
@File:base.py
"""
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, locator, timeout=10, poll_frequency=0.5):
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        return wait.until(Ec.element_to_be_clickable(locator))

    def visit_url(self, url):
        return self.driver.get(url)

    def click(self, locator):
        try:
            ele = self.wait_element(locator)
            ele.click()
        except (NoSuchElementException, TimeoutError):
            raise "{}".format('元素不可点击')

    def send_keys(self, location: str, value) -> None:
        """
        input the value to input box of element
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :param value: 输入的数据
        :return: None
        """
        try:
            element = self.wait_element(location)
            element.clear()
            element.send_keys(value)
        except (NoSuchElementException, TimeoutException) as e:
            # self.logger.error("输入框:{}, 输入数据{}失败:{}".format(location, value, e))
            # self.save_screen_shot("send_keys")
            raise e

    def get_element_text(self, locator):
        ele = self.wait_element(locator)
        try:
            value = ele.text
        except AttributeError:
            value = ele.get_attribute('value')
        # self.logger.info('')
        return value

    # def save_screen_shot(self, info: str = ''):
    #     """
    #     屏幕截图
    #     :param info:
    #     :return:
    #     """
    #     current_time = self.c_dir.get_current_time()
    #     img_path = self.c_dir.create_dir(ERROR_IMG_DIR)
    #     filename = img_path + '/' + current_time + info + '.png'
    #     return self.driver.save_screenshot(filename)
