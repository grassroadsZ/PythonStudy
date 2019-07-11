'''
-*-conding:utf-8
@Time:2019-05-21 6:43
@auther:grassroadsZ
@file:handle_config.py
'''
from configparser import ConfigParser

class ExcelConfig(ConfigParser):
    def __init__(self):
        # 继承父类，同时重写父类self.filename属性
        super().__init__()
        # self.filename = r"F:\Python3.6\LemonPython_Study\Homework\case_config.conf"
        self.filename = "F:\Python3.6\LemonPython_Study\Homework\lesson_21_0520_fina_rewrite\case_config.conf"
        self.read(self.filename,encoding = "utf-8")

    def __call__(self , section , option=None , is_eval=False , is_bool=False):
        if option is None:
            return dict( self[section] )

        if isinstance(is_bool,bool):
            if is_bool:
                return self.getboolean( section , option )
            # else:
            #     return self.get( section , option )
        else:
            raise ValueError("is_bool的值必须是布尔类型")

        data = self.get( section , option )
        if data.isdigit():
            return int( data )
        try:
            return float( data )
        except Exception:
            pass

        if isinstance(is_eval,bool):
            if is_eval is True:
                return eval( self.get( section , option ) )
            # else:
            #     return self.get( section , option )
        else:
            raise ValueError("is_bool的值必须是布尔类型")

        return data
do_config = ExcelConfig()