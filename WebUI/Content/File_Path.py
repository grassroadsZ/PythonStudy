"""
-*-conding: utf-8
@Time:2019-07-04 7:02
@Auther:grassroadsZ
@File:File_Path.py
"""

import os

# 项目根目录
Base_Path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件目录
ConfigFilePath = os.path.join(Base_Path, "config")

# 自定义封装后文件目录
Content = os.path.join(Base_Path, "Content")

# 图片文件夹
IMG = os.path.join(Base_Path, "img")

# 文件目录
File_path = os.path.abspath(__file__)




if __name__ == '__main__':
    print(Base_Path)
    print(ConfigFilePath)
    print(File_path)
    print(IMG)

