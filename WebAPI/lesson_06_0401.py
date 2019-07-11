# -*-conding:utf-8
# @Time:2019/4/7 13:26
# @auther:grassroadsZ
# @file:lesson_06_0401.py

# 1.函数有哪几种参数类型，分别有什么特点？

# 函数的参数类型分为必须参数，可以接收可变类型，不可变类型的元素
#                 关键字参数，通过关键字来调用值
#                 默认参数，函数默认传值
#                 不定长参数。*以元组形式接收位置参数，**以字典形式接收关键字参数。

# 2.在函数调用时，位置参数和关键字参数的顺序
# 函数调用时应将位置参数放在关键字参数前面

# 3.什么是拆包（unpack）和打包（pack）？
# 拆包是指使用for循环或者与序列及字典中元素值个数相等或一个变量去接收赋值时的行为
# 打包是指函数调用时以*参数名以一个元组或者以**以一个字典的形式将来接收传入的参数的行为

# 4.哪些类型可以拆包（unpack）？拆包时变量的个数要什么要求？
# 序列及字典均可拆包。拆包时变量的个数为1或者与拆包中元素个数相等

# 5.函数的可变参数是什么？有哪几种？为什么要使用可变参数？
# 函数的可变参数为接收的参数个数不确定，有*args以一个元组的形式导入或者以*kw_args以一个字典的形式导入
'''
# 6.将两个变量的值进行交换（a = 100, b = 200）
# a.交换之后，a = 200， b = 100
# b.使用你能想到的所有方法来实现

a = 100
b = 200
a,b = b,a
print(a,b)
'''

'''
# 7.编写如下程序
# 将用户输入的所有数字相乘之后对20取余数
# a.用户输入的数字个数不确定
# b.请使用函数来实现


def num_sum(*arg):
    """
    对用户输入的数字进行想乘后所得结果对20取余
    :param arg:
    :return:
    """
    number = input("请输入数字，以逗号分开")
    num = 1
    if number.isalnum():
        for i in number.split(","):
            num *= int(i)
        print(num%20)
    else:
        number = input( "只能输入数字，以逗号分隔，请重新输入" )
        for i in number.split(","):
            num *= int(i)
        print(num%20)

num_sum()
'''

'''
# 8.编写如下程序
# 求列表所有元素的和
# a.one_list = [13, 21, 3, 76, 54, 12, 44, 80, 92]
# # b.使用while循环来实现
one_list = [13, 21, 3, 76, 54, 12, 44, 80, 92]
def while_sum():
    count = 1
    num = 0
    while count < len(one_list):
        for i in one_list:
            num += i
            count +=1
        print(num)

while_sum()
'''

''''
# 9.编写如下程序
# 求圆的面积
# a.传入一个圆的半径，将其面积返回
# b.函数中的Π，可以导入import math，通过math.pi来获取（也可以直接使用3.14）

import math
def square_sum(*R , Π=math.pi):
    """
    计算圆的面积
    :param r:
    :param Π:
    :return:
    """
    R = float( input( "请输入一个圆的半径：" ) )
    area = Π * (R ** 2)
    print(area)


square_sum()
'''

# 11.编写如下程序（必做题第7题拓展）
# 将用户输入的所有数字相乘之后对20取余数
# a.用户输入的数字个数不确定
# b.用户可能使用关键字参数来传递待相乘的数字，例如：num1=21,num2=45等等,请使用函数来实现

def num_sum(*args,**kwargs):
    """
    将输入的参数进行相乘后取余
    :param arg:
    :param kwargs:
    :return:
    """
    num = 1
    global num
    reslut_args = 1
    reslut_kwargs = 1
    dict1 = dict(kwargs)
    for i in args:      # 遍历计算位置参数处的值
        reslut_args *= i
    for value in dict1.values():    # 遍历计算关键字参数处的值
        reslut_kwargs *= value
    print(reslut_args*reslut_kwargs)    # 计算位置参数与关键字参数处想乘的值

num_sum()