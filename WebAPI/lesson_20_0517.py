'''
-*-conding:utf-8
@Time:2019-05-20 6:34
@auther:grassroadsZ
@file:lesson_20_0517.py
'''

import logging
from logging.handlers import RotatingFileHandler
# 1.定义日志器并尝试封装

class MyLog(object):
    """
    我的日志类
    """
    def __init__(self):
        """
        :param name:日志收集器的名字
        :param level: 日志收集器的等级
        """
    # 定义名为case的日志收集器对象
        self.loger = logging.getLogger()
    # 定义日志收集器等级
        self.loger.setLevel(self.content_level)
    # 定义输出到终端
        self.out_where = logging.StreamHandler()
    # 定义日志输出出道等级
        self.out_where.setLevel(self.out_level)
    # 定义日志显示格式
        self.out_format = logging.Formatter("%(asctime)s - [%(levelname)s] -[日志信息]: %(message)s")
        self.out_where.setFormatter(self.out_format)
        self.loger.addHandler(self.out_where)

    def out(self):
        self.loger.info("msg")
        self.loger.debug( "debug" )
        self.loger.warning("warn")
        self.loger.error("error")


if __name__ == '__main__':
    log = MyLog("case")
    log.out()


