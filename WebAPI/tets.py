'''
-*-conding:utf-8
@Time:2019/4/11 18:03
@auther:grassroadsZ
@file:tets.py
'''
# from Homework import lesson_08_0410 as a
#
#
# print(a.round1(1))
# print(a.Square(5,9.5793))
# print(a.pblx(20))

import os
te = os.path.split('Homework/Lesson_01_0318.docx')[0]
print(os.path.join(r'F:\Python3.6\LemonPython_Study\apibook','tets.py'))
print(os.path.join('te','tets.py'))


# def pblx():
#     """
#     根据用户输入的数字求出小于及等于的裴波拉切数列
#     判断没时间写，用户输入的错误及异常情况处理可参考老师的代码。
#     :param num:
#     :return:
#     """
#     try:
#         num = int( input( "请输入一个数字" ) )
#         a , b = 0 , 1
#         list1 = []
#         for i in range( num ):
#             a , b = b , a + b
#             list1.append( a )
#             if b >= num:
#                 return "{}的裴波拉西数列是{}".format( num , list1 )
#     except BaseException as e:
#         print(e)
#         pblx()
#
#
#
#
#
# pblx()
