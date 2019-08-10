"""
-*-conding: utf-8
@Time:2019-06-06 6:27
@Auther:grassroadsZ
@File:handle_replace.py
"""
import re
from options.handle_config import HandleConfig
from options.handle_mysql import HandleMysql
from options.File_path import User_File_Path


class DataReplace:
    """
    实现参数化替换
    """
    not_existed_phone = re.compile(r"\$\{mobile\}")
    existed_phone = re.compile(r"\$\{exist_mobile\}")
    verify_code = re.compile(r"\$\{verify_code\}")
    Uid = re.compile(r"\$\{registered_uid\}")



    do_mysql = HandleMysql()

    @classmethod
    def not_existed_phone_replace(cls, data):
        """
        参数化替换为不存在的手机号
        :param data:
        :return:参数化替换数据库中不存在的手机号
        """
        if re.search(cls.not_existed_phone, data):
            data = re.sub(cls.not_existed_phone, cls.do_mysql.create_not_existed_mobile(), data)
        return data

    @classmethod
    def verify_replace(cls , data):
        """
        参数化替换为投资人的手机号
        :param data:
        :return:替换从用户配置表中获取的投资人的的手机号
        """
        # code = getattr(cls, "code")
        if re.search(cls.verify_code, data ):
            data = re.sub(cls.verify_code, str(cls.code), data )
        return data

    @classmethod
    def exist_phone_replace(cls , data):
        """
        参数化替换管理员的的手机号和借款人的id
        :param data:
        :return:替换从用户配置表中获取的管理员的的手机号和借款人的id
        """
        if re.search(cls.existed_phone, data):
            data = re.sub(cls.existed_phone, cls.mobile, data)
        return data

    @classmethod
    def uid_replace(cls, data):
        """
        替换用户的uid
        :param data:
        :return:
        """
        if re.search(cls.Uid, data):
            uid = str(getattr(cls, "uid"))
            data = re.sub(cls.Uid,uid, data)

        return data

    @staticmethod
    def phone_replace(data):

        data = DataReplace.not_existed_phone_replace(data)
        data = DataReplace.verify_replace(data)
        data = DataReplace.exist_phone_replace(data)
        data = DataReplace.uid_replace(data)
        # data = DataReplace.add_testcase_replace(data)
        # data = DataReplace.loanId_replace(data)

        return data



if __name__ == '__main__':
    not_existed = '{"mobilephone": "${mobile}", "pwd":"123456", "regname": "KeYou"}'
    exited = '{"mobilephone": "${exist_phone}", "pwd":"123456"}'
    touzi = '{"mobilephone": "${touzi_phone}", "pwd":"123456"}'
    add = '{"mobilephone": "${admin}", "pwd":"${project_id}"}'
    # print(DataReplace.not_existed_phone_replace(not_existed))
    # print(DataReplace.existed_phone_replace(exited))
    # print( DataReplace().phone_replace( not_existed ) )
    # print( DataReplace().phone_replace(exited))
    # print(DataReplace().phone_replace(touzi))





