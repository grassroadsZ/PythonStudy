'''
-*-conding:utf-8
@Time:2019/4/14 16:46
@auther:grassroadsZ
@file:file.py
'''

file = open(r'F:\Python3.6\LemonPython_Study\Homework\url.txt',mode = 'r',encoding = 'utf-8')
for a in file:
    print(a,type(a))