"""
-*-conding:utf-8
@Time:2019/4/11 12:46
@auther:grassroadsZ
@file:lesson_08_0410.py
"""

import math

# 1.什么是模块？有什么作用？
# python中一个py文件即是一个模块，模块可以被导入到其它模块处被调用。

# 2.模块中的哪些资源可以被调用处使用？
# 模块中的函数，类，全局变量均可被别处调用使用

# 3.模块的命名规范
# 模块命名规范与变量命名规则类似。
# 不推荐使用数字，特殊符号，__以及中文开头。
# 避免不与内置方法，函数名重名

# 4.模块的导入方式有哪几种？
# 使用 import 导入
# 使用from 绝对路径 import 模块
# 可导入模块所有，也可只导入模块内的函数，类或全局变量

# 5. __name__属性的特性？
# __name__后的程序在当前模块会被运行，但是在模块被其它模块导入后，__name__后的程序不会在被导入的模块中执行

# 6.将两个变量的值进行交换（a = 100, b = 200）
a = 100
b = 200
a,b = b, a

b = b - a
a = a + b

# 8.os模块中有哪些常用的方法？用什么作用？
'''
# os的常用方法：
os.path.join()  # 目录和文件拼接
os.path.split() # 目录和文件切割
os.remove() # 删除文件目录
os.removedirs() # 删除层级目录
os.listdir()    # 列出当前路径目录
os.path.isdir() # 判断当前是否在文件目录下
os.path.isfile()    # 判断当前是否为文件
os._exists()    # 判断文件或目录是否存在
os.environ  # 环境变量
os.mkdir()  # 生成文件目录
'''


# 9.编写如下程序
# a.在一个模块中，定义求圆的面积和周长、长方形的面积和周长的函数，然后分别在另一个程序中调用
# b.每个模块中需要添加测试代码

def round1(r):
    """
    根据圆的半径计算面积和周长
    :param r:
    :return:
    """
    Π = math.pi
    round_area = float(Π * (r ** 2))    # 圆的面积
    round_perimeter = float(2 * Π * r)  # 周长
    result = "圆的面积是{:.2f},周长是{:.2f}".format(round_area,round_perimeter)
    return result

def Square(long, width):
    """
    根据长宽计算长方形周长和面积
    :param long:
    :param width:
    :return:
    """
    Square_area = long * width
    Square_perimeter = 2 * (long + width )
    return "长方形面积是{:.2f}周长是{:.2f}".format(Square_area, Square_perimeter)




# 9.编写如下程序
# 裴伯拉切数列，从第三个元素开始，每个元素为前两个元素之和，用户输入某个大于0的正整数，求出小于等于这个正整数的所有裴伯拉切元素
# a.裴伯拉切数列为：0  1  1  2  3  5  8  13  21  34  55  89  144
# b.例如，用户输入50，那么小于等于50的裴伯拉切元素为：0  1  1  2  3  5  8  13  21  34
# c.要求在一个模块中定义，在另一个程序中调用

def pblx(num):
        """
        根据用户输入的数字求出小于及等于的裴波拉切数列
        判断没时间写，用户输入的错误及异常情况处理可参考老师的代码。
        :param num:
        :return:
        """
        num = int(input( "请输入一个数字" ))
        a,b = 0,1
        list1 = []
        for i in range(num):
            a,b = b, a + b
            list1.append(a)
            if b >= num:
                return "{}的裴波拉西数列是{}".format(num, list1)

if __name__ == '__main__':
    print(round1(2))
    print(Square(3,4))
    print( pblx( 20 ) )