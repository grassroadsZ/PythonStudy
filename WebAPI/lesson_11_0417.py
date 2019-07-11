'''
-*-conding:utf-8
@Time:2019/4/18 20:48
@auther:grassroadsZ
@file:lesson_11_0417.py
'''

# 1.什么是类？什么是对象？
# 类是一系列具有共同行为特征的事物的一个统称

# 2.类由哪几部分构成？
# 类由关键词class以及类名和类的特征(属性)和行为(方法)组成

# 3.类的设计原则
# 请从类的命名、类中属性和方法来阐述
# 类名需要见名知意，采用驼峰命名法，类名内不存在下划线。类中的属性由类的特征所决定，类的方法由类的行为所确定

# 4.类中实例方法的特性？__init__方法的作用？
# 类中实例方法的特性是类中实例方法可通过关键字self实例化本身构成一个对象后，通过对象可以在类中以及类的外面被使用。子类继承父类后同样可使用。

# __init__ 相当于一个构造器，在创建一个类时，通过__init__ 构造器将类本身实例化从而构成一个对象。从而使类能够被调用。

# 5.列举几个生活中类和对象的例子
# 汽车是一个父类，电动系汽车是个子类，电动系汽车的某一辆是个对象

# 6.编写如下程序
# 灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
# a.根据以上信息，抽象出一个类
# b.定义相关属性，并能在类的外面调用
# c.定义相关方法，在方法中打印相应信息


class Cat():
    """
    定义一个猫类
    """
    def __init__(self,name,age,color):
        "初始化属性name，age，color"
        self.name = name
        self.age = age
        self.color =color


    def action(self,*food):
        "动作"
        print("年龄为{}岁的{} eat {},drink {}".format(self.age,self.name,*food))

    def feel(self):
        "感觉"
        print("享受")


if __name__ == '__main__':
    food = ("nice food","orange")
    cat = Cat("Tom",1,"gray")
    cat.action(*food)
    cat.feel()