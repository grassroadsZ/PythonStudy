# -*-conding:utf-8
# @Time:2019-06-02 22:26
# @auther:grassroadsZ
# @file:test_re.py

import re

demo_str = '{"test":"123", "${mobile1}":"13000000000", "pa":1}'
# 将正则字符串编译成Pattern对象
Pattern = re.compile(r"\$\{mobile\}")
# 一、使用Pattern对象匹配文本,匹配到则返回匹配对象，否则返回None
match_obj = re.search(Pattern,demo_str)
# 二、直接将匹配对象进行进行匹配并替换
new_str = re.sub(Pattern, "5555", demo_str)

print(new_str)
