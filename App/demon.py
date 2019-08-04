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

desired_caps = {
    'platformName':'Android',
    'platformVersion':'5.1',
    'deviceName':'Android Emulator',
    # 'automationName':'',
    'appPackage':'com.xxzb.fenwoo',
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",

}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)

time.sleep(3)
driver.swipe(900,1700,100,1700)
time.sleep(1)
driver.swipe(900,1700,100,1700)
time.sleep(1)
driver.swipe(900,1700,100,1700)
time.sleep(1)
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_start').click()
time.sleep(1)
driver.find_element_by_xpath('//android.widget.TextView[@text=\"我\"]').click()
time.sleep(1)
driver.find_element_by_id('com.xxzb.fenwoo:id/et_phone').send_keys('18684720553')
time.sleep(1)
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_next_step').click()
time.sleep(1)
driver.find_element_by_id('com.xxzb.fenwoo:id/et_pwd').send_keys('python')
time.sleep(1)
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_next_step').click()
driver.quit()
