'''
-*-conding:utf-8
@Time:2019-05-21 7:02
@auther:grassroadsZ
@file:handle_log.py
'''

import logging
from logging.handlers import RotatingFileHandler
from Homework.lesson_21_0520_fina_rewrite.handle_config import do_config

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
        self.loger = logging.getLogger(do_config("log","name"))
    # 定义日志收集器等级
        self.loger.setLevel(do_config("log","content_level"))
    # 定义输出到终端
        consle_handle = logging.StreamHandler()
        file_handle = RotatingFileHandler(filename = do_config("log","log_name"),
                                          mode = "a",
                                          maxBytes = do_config("log","Maxbytes"),
                                          backupCount = do_config("log","count"),
                                          encoding = do_config("log","encoding")
                                          )
    # 定义日志输出出道等级
        consle_handle.setLevel(do_config("log","content_level"))
        file_handle.setLevel(do_config("log","content_level"))
    # 定义日志显示格式
        consle_format = logging.Formatter(do_config("log","simple"))
        file_format = logging.Formatter(do_config("log","clear"))

        consle_handle.setFormatter(consle_format)
        file_handle.setFormatter(file_format)
        self.loger.addHandler(consle_handle)
        self.loger.addHandler(file_handle)

    def out(self):
        return self.loger

do_log = MyLog().out()



if __name__ == '__main__':
    do_log.info("msg")
    do_log.debug( "debug" )
    do_log.warning("warn")
    do_log.error("error")
