'''
-*-conding:utf-8
@Time:2019/4/21 13:24
@auther:grassroadsZ
@file:lesson_12_0419.py
'''

# 1.__str__的作用？
# 用于打印输入类本身

# 2.is 与 == 的区别？
# is 是成员运算符，两个对象之间比较的是对象在内存中的地址id
# == 是比较运算符，比较的是两个对象的值，内容是否相等

# 3.类属性是什么？如何定义？在类外和类里如何调用？
# 类属性是类的一个特征(变量)，类内和类外均使用  类名.类属性  来调用


# 4.类方法是什么？作用？如何定义？
# 类方法是使用关键字@classmethod + 方法来定义的一个方法，用来修改类属性。



# 6.编写如下程序
# 创建一个名为 Restaurant的类，要求拥有饭店名（restaurant_name） 和美食种类（cooking_type）两个属性。
# a.需要创建一个名为 describe_restaurant()的方法（描述饭店名和美食种类相关信息）和一个名为 open_restaurant()的方法（显示饭店正在营业）。
# b.根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。


class Restaurant:
    "一个由两个类属性和两个方法组成的类"
    restaurant_name = '小吃店'
    cooking_type = 'Nothing'

    def __init__(self):
        self.name = Restaurant.restaurant_name
        self.food = Restaurant.cooking_type


    def describe_restaurant(self):
        """
        描述饭店的店名和美食种类
        :return:
        """
        print("饭店的名字叫{}, 含有的美食是{}".format(self.name,self.food))

    def open_restaurant(self,status):
        """
        饭店的状态,0:关闭，1：打开
        :return:
        """
        if status == 0:
            return "关闭"
        if status == 1:
            return "营业"

# 7.编写如下程序
# 编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。
class MathCount:
    "一个对数学进行加减乘除计算类，可能对题意理解不正确，感觉这种编写方式调用很不舒服"
    def __init__(self,x,y):
        """
        :param x:第一个数字
        :param type: 不同的类型调用不同的方法
        :param y: 第二个数字
        """
        self.x = x
        self.y = y

    def add(self):
        "加"
        print( "{}加{}的结果是{:.4f}".format(self.x,self.y,self.x + self.y))

    def less(self):
        "减法"
        print( "{}减{}的结果是{:.4f}".format(self.x , self.y ,self.x - self.y))

    def multiply(self):
        "乘法"
        print( "{}乘{}的结果是{:.4f}".format(self.x,self.y , self.x * self.y))

    def divide(self):
        print( "{}除以{}的结果是{:.4f}".format( self.x , self.y  , self.x / self.y ))





# 二、选作题
# 8.编写如下程序
# 编写一个工具箱类，需要有工具的名称、功能描述、价格，能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。

# 没有理解题意做的多半是有问题的
class Tool:
    "一个可以增加删除，查看计数的工具箱类"
    toolbox = []
    def __init__(self,name,price,describe):
        """
        :param name: 工具箱名称
        :param price:工具箱价格
        :param describe:工具箱的描述
        """
        self.dict1 = {}
        self.name = name
        self.price = price
        self.describe = describe
        self.dict1["名称"] = self.name
        self.dict1["价格"] = self.price
        self.dict1["描述"] = self.describe
        Tool.toolbox.append(self.dict1)



if __name__ == '__main__':
    # 饭店类
    restaurant = Restaurant()
    print( "类属性-店名：{}\n类属性-食物种类：{}".format( Restaurant.restaurant_name , Restaurant.cooking_type ) , end = "\n" )
    restaurant.describe_restaurant()
    print( restaurant.open_restaurant( 1 ) )

    # 科学计算器
    math = MathCount( 1 , 2.95 )
    math.divide()

    # 工具箱类
    tool = Tool( 'ceshi' , 6 , '多半是不对' )
    print(tool.toolbox,len(tool.toolbox ))
    tool = Tool( 'hah' , 9 , '多半hai是不对' )
    print(tool.toolbox)
    del tool.toolbox[0]
    print(tool.toolbox)