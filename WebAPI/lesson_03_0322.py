# -*-conding:utf-8
# @Time:2019/3/23 12:01
# @auther:grassroadsZ
# @file:lesson_03_0322.py

'''
# 一.个人信息展示
# 在控制台一次提示用户输入：姓名、网名、年龄、性别、爱好、座右铭
# 按照以下格式输出
# 个人信息展示
# **************************************************
# 姓名（网名）
# 年龄：年龄
# 性别：性别
# 爱好：爱好
# 座右铭：座右铭
# **************************************************
name,age,sex,hobby,Motto = input("请输入网名："),input("请输入年龄："),\
                           input("请输入性别："),input("请输入爱好："),input("请输入座右铭：")

print("*"*100)
print("\n姓名(",name,")","\n年龄:",age,"\n性别:",sex,"\n爱好:",hobby,"\n座右铭:",Motto)
print("*"*100)
'''

'''
# 2.Python中的序列类型有哪些？支持哪些操作？
# 序列类型有不可变序列str和tuple，可变序列list
# 支持操作：
#             索引取值
#             切片取值
#             成员关系
#             拼接操作
#             重复操作
#             求长度
#             内置函数
'''

'''
# 3.编写代码，用户输入1-7七个数字，分别代表周一到周日，如果输入的数字是6或7，打印输出“周末”
# 方法一：
list_date = ["","","","","","周末","周末"]
num = int(input("请输入数字1-7："))
# print(len(list_date))
print("{}".format(list_date[num-1]))
#方法二：
def date_time():
    num = int(input("请输入数字1-7："))
    while num not in range(1,8):
        print("只能输入1-7的数字，请重新输入：")
        num = int(input())
    if num == 6 or 7:
        print("周末")
date_time()
'''

'''
# 4.列表中append和extend方法的区别，请举例说明
# append 是将元素直接追加到列表的最后面，extend是将列表中的元素逐一拆分后放入列表中
list1=[1,2,3]
list1.append(["f"])
print(list1)   #输出：[1, 2, 3, ['f']]
list1.extend("hello")
print(list1)    #输出：[1, 2, 3, ['f'], 'h', 'e', 'l', 'l', 'o'] 
'''

'''
# 5.删除如下列表中的"矮穷丑"，写出能想到的所有方法
keyou_info = ["可优", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
# 方法一：del keyou_info[3]
# 方法二：keyou_info.remove("矮穷丑")
# 方法三：keyou_info.pop(3)
# print
'''

'''
# 6.元组和列表有什么区别？分别应用于哪些场景？
# 元组是不可变类型，不支持通过索引去删除以及替换，常用于存储不希望改变的数据。元组内可以嵌套可变类型的数据，不推荐
# 列表是可变类型，可以通过索引去删除及替换，用于存储可变数据
'''

'''
7.创建元组有哪些方式？
value = () 当元组内只有一个元素时需要在这个元素的后面加上，
tuple() 
'''
'''
my_info = {"name": "grassroadsZ", "sex": "man", "age": 23, "hight": 170}
other_info = {"character": "activity", "Motto": "Growth is very hard，but very nice!"}
# merge_info = dict(my_info,**other_info) #字典合并方法dict(dict1,**dict2)
my_info["age"] = 18
print(my_info["age"], "\n", other_info["Motto"])
'''
# 百度脑图地址：
# http://naotu.baidu.com/file/9496bf39247484fecaa60bc4d2510b99?token=f889bb3520597ce1


a = int(input("输入数字："))
if a == 1:
    print("1")
elif a == 2:
    print("2")
else:
    print("其它")

