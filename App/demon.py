"""
-*-enconding: utf-8
@Time:2019-08-02 7:51
@Author:grassroadsZ
@File:demon.py
Motto：good good study , day day up !!!
"""

# app测试demo
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.xxzb.fenwoo',
    'appActivity': 'com.xxzb.fenwoo.activity.user.SafetyCenterActivity'
    # "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
}
driver = webdriver.Remote(
    'http://127.0.0.1:4723/wd/hub',
    desired_capabilities=desired_caps)

time.sleep(3)
# for _ in range(3):
#     driver.swipe(900, 1700, 100, 1700)
#     time.sleep(1)
# driver.find_element_by_id('com.xxzb.fenwoo:id/btn_start').click()
# time.sleep(1)
# driver.find_element_by_xpath('//android.widget.TextView[@text=\"我\"]').click()
# time.sleep(1)
# driver.find_element_by_id('com.xxzb.fenwoo:id/et_phone').send_keys('18684720553')
# time.sleep(1)
# driver.find_element_by_id('com.xxzb.fenwoo:id/btn_next_step').click()
# time.sleep(1)
# driver.find_element_by_id('com.xxzb.fenwoo:id/et_pwd').send_keys('python')
# time.sleep(1)
# driver.find_element_by_id('com.xxzb.fenwoo:id/btn_next_step').click()
driver.find_element_by_id('com.xxzb.fenwoo:id/layout_gesture_password').click()
time.sleep(1)
driver.find_element_by_id('com.xxzb.fenwoo:id/layout_update_gesture').click()
time.sleep(1)
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_gesturepwd_guide').click()
time.sleep(1)
driver.find_element_by_id('com.xxzb.fenwoo:id/right_btn').click()
time.sleep(1)
pict_size_ele = driver.find_element_by_id('com.xxzb.fenwoo:id/gesturepwd_create_lockview')
pict_size = pict_size_ele.rect
start_x = pict_size['x']
start_y = pict_size['y']
height = pict_size['height']
width = pict_size['width']
point_1 = {"x": start_x + width * 1/6, "y": start_y + height * 1/6}
point_2 = {"x": start_x + width * 3/6, "y": start_y + height * 1/6}
point_3 = {"x": start_x + width * 5/6, "y": start_y + height * 1/6}
point_4 = {"x": start_x + width * 1/6, "y": start_y + height * 3/6}
driver_1 = TouchAction(driver)
driver_1.press(**point_1).wait(500).move_to(
            **point_2).wait(500).move_to(
            **point_3).wait(500).move_to(
            **point_4).wait(500).release().perform()
time.sleep(1)
driver.find_element_by_id('com.xxzb.fenwoo:id/reset_btn').click()
driver.find_element_by_id('com.xxzb.fenwoo:id/reset_btn').click()


time.sleep(10)
driver.quit()
