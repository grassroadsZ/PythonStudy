"""
-*-conding: utf-8
@Time:2019-07-02 19:51
@Auther:grassroadsZ
@File:lesson03_0701.py
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from Content.handle_config import do_config


def wait_ele_tobe_click(driver, locator):
    wait = WebDriverWait(driver, 5)
    try:
        ele = wait.until(Ec.element_to_be_clickable((By.XPATH, locator)))
    except Exception as a:
        mistake = f"something Error {a}"
        raise mistake
    else:
        ele.click()


bs = webdriver.Chrome()
# 隐式等待5s
bs.implicitly_wait(5)
# 打开课堂派
bs.get("https://www.ketangpai.com/")
# 点击登陆
bs.find_element_by_xpath('//a[@class="login"]').click()
# 输入账号
bs.find_element_by_xpath('//input[@name="account"]').send_keys(do_config("user_message", "amount"))
# 输入密码
bs.find_element_by_xpath('//input[@name="pass"]').send_keys(do_config("user_message", "password"))
# 点击登陆
bs.find_element_by_xpath('//a[@class="btn-btn"]').click()
# 等待弹窗出来点击关闭
time.sleep(2)
wait_ele_tobe_click(bs, '//a[@class="close"]')
time.sleep(2)
wait_ele_tobe_click(bs, '//a[contains(text(),"全栈")]')







