"""
-*-enconding: utf-8
@Time:2019-08-04 19:53
@Author:grassroadsZ
@File:file.py
Motto：good good study , day day up !!!
"""

import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join('Content', BASE_PATH)
PAGEES = os.path.join('Pages', BASE_PATH)
CONFIG = os.path.join('Config', BASE_PATH)
FILE_PATH = os.path.abspath(__file__)


if __name__ == '__main__':
    pass
