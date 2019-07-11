"""
-*-conding: utf-8
@Time:2019-07-10 7:50
@Auther:grassroadsZ
@File:base.py
"""
import win32gui
import win32con
import time

def uploadfile(file):
    dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
    time.sleep(1)
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    # time.sleep(1)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    # time.sleep(1)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    # time.sleep(1)
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    time.sleep(1)
    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file)  # 往输入框输入绝对地址
    time.sleep(1)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
