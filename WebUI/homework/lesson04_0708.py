"""
-*-conding: utf-8
@Time:2019-07-09 14:59
@Auther:grassroadsZ
@File:lesson04_0708.py
"""

import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from WebUI.Content.File_Path import IMG
from WebUI.Content.base import uploadfile
from WebUI.Content.handle_config import do_config


def wait_ele_tobe_click(driver, locator):
    wait = WebDriverWait(driver, 5)
    try:
        ele = wait.until(Ec.element_to_be_clickable((By.XPATH, locator)))
    except Exception as a:
        mistake = f"something Error {a}"
        raise mistake
    else:
        ele.click()


def tencent_login():
    """腾讯课堂登陆"""
    bs = webdriver.Chrome()
    # 隐式等待5s
    bs.implicitly_wait(5)
    # 打开腾讯课堂
    bs.get("https://ke.qq.com/")
    # 点击登陆
    wait_ele_tobe_click(bs, '//a[@report-attr="module=login&position=card"]')
    # 点击qq登陆
    wait_ele_tobe_click(bs, '//a[@data-type="1"]')
    wait = WebDriverWait(bs, 3)
    # 切换iframe
    wait.until(Ec.frame_to_be_available_and_switch_to_it((By.NAME, "login_frame_qq")))
    # 点击账号密码登陆
    wait_ele_tobe_click(bs, '//a[@id="switcher_plogin"]')
    # 输入账号密码
    bs.find_element_by_id('u').send_keys(do_config("Tencent", "user"))
    bs.find_element_by_id('p').send_keys(do_config("Tencent", "pwd"))
    # 点击登陆
    bs.find_element_by_id('login_button').click()
    bs.quit()

class ClassPai:
    """保存课堂派微信二维码的类"""
    def __init__(self):
        self.bs = webdriver.Chrome()
        self.bs.implicitly_wait(5)

    def login(self):
        """打开课堂派进入登录页面"""
        self.bs.get("https://www.ketangpai.com/")
        # 点击登陆
        self.bs.find_element_by_xpath('//a[@class="login"]').click()

    def get_image(self):
        """获取微信二维码图片"""
        self.login()
        self.bs.find_element_by_link_text("微信登录").click()
        wait = WebDriverWait(self.bs, 5)
        wait.until(Ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//div[@id='login_container']//iframe")))
        time.sleep(2)
        img_url = self.bs.find_element_by_xpath("//div[@class='wrp_code']//img").get_attribute("src")
        return img_url

    def save_image(self):
        """将二维码图片保存"""
        res = requests.get(self.get_image())
        with open(os.path.join(IMG, "WeChat.png"), "wb") as f:
            f.write(res.content)

    def bs_close(self):
        """关闭浏览器"""
        self.bs.quit()

def upload_file():
    bs = webdriver.Chrome()
    # 隐式等待5s
    bs.implicitly_wait(5)
    bs.get("file:///F:/Python3.6/LemonPython_Study/WebUI/homework/lesson02_0626.html")
    # 方法一：使用send_keys方法上传文件
    bs.find_element_by_id('upload_file').send_keys(
        r"F:\Python3.6\LemonPython_Study\WebUI\img\WeChat.png")
    time.sleep(10)
    bs.find_element_by_id("upload_file").clear()
    # 方法二：使用pypiwin32模块上传文件
    bs.find_element_by_id('upload_file').click()
    time.sleep(3)
    uploadfile(r"F:\Python3.6\LemonPython_Study\WebUI\img\WeChat.png")

def change_ele():
    bs = webdriver.Chrome()
    # 隐式等待5s
    bs.implicitly_wait(5)
    bs.get("https://www.12306.cn/index/")
    time.sleep(1)
    js_code = 'ele = document.getElementById("train_date");ele.readOnly=false;ele.value="2019-01-01"'
    bs.execute_script(js_code)
    time.sleep(0.5)


# if __name__ == '__main__':
    # tencent_login()
    # classpai=ClassPai()
    # classpai.save_image()
    # upload_file()
    # wait_ele_tobe_click()
    # change_ele()
