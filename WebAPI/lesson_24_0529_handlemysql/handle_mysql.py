# -*-conding:utf-8
# @Time:2019-05-30 20:26
# @auther:grassroadsZ
# @file:handle_mysql.py

import pymysql
from Homework.lesson_24_0529_handlemysql.handle_config import do_config


class Mysql:
    """
    我的mysql处理类
    """
    def __init__(self):
        self.connt = pymysql.connect(
            host = do_config("mysql", "host"),
            port = do_config("mysql", "port"),
            db = do_config("mysql", "db"),
            user = do_config("mysql", "username"),
            password = do_config("mysql", "test"),
            charset = "utf8",
            cursorclass = pymysql.cursors.DictCursor)
        # 创建游标
        self.cursor = self.connt.cursor()

    def __call__(self, sql, args = None, is_more = False):
        # 执行sql语句
        self.cursor.execute(sql, args)
        # 手动提交
        self.connt.commit()
        if is_more:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()
        return result

    def close(self):
        self.cursor.close()
        self.connt.close()


if __name__ == '__main__':
    sql_1 = "SELECT * from member LIMIT 10;"
    mysql = Mysql()
    print(mysql(sql_1,is_more = True))