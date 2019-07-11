# -*-conding:utf-8
# @Time:2019/3/31 15:33
# @auther:grassroadsZ
# @file:lesson_05_0329.py

# 1.break和continue的区别
# break与continue都可以用在循环中，break时直接跳出循环且循环终止，而continue只是当前此次循环停止，循环中contiune后的所有代码此次循环均不会再执行

# 2.while和for循环的异同点
# while与for循环均可以写成无限循环，while循环与if条件判断较像，都是某个条件达到后才终止，for循环支持遍历，可以遍历序列，
# 可进行元祖解包，while循环多用于不确定循环次数的场景，for循环多用于循环次数确定的场景

# 3.函数有哪些特性
# 1.可被重复调用;
# 2.使代码看起来更简洁；
# 3.可自定义函数

# 4.Pycharm中Debug调试的Step Over(F8)、Step Into(F7)区别
# Step Over：直接跳过断点至末尾
# StepInto：进入到函数的内部

# 5.写出将列表翻转的所有方法
# 将列表[13, 20, 42, 85, 9, 45]翻转之后为[45, 9, 85, 42, 20, 13]
# num_list = [13, 20, 42, 85, 9, 45]
# 方法一：new_list = num_list[::-1]
# 方法二：new_list = list(num_list.__reversed__())   系百度所得
# 方法三：先求出列表长度，确定对换次数，通过range来控制for循环对换次数，此代码有问题，个人感觉理论上次思路可行，待后续完善
''' # 确定值对换的次数
# count = 0
# change_times = int(len(num_list)%2)
# if change_times == 0:
#     count1 = int(len(num_list)/2)
# else:
#     count1 = int(len(num_list)//2)
# # while count <= count1:
# for i in range(0,count1+1):
#     if count == count1:
#         break
#     elif i == 0:
#         num_list[i] , num_list[-1] = num_list[-1] , num_list[i]
#     else:
#         num_list[i],num_list[i-1] = num_list[i-1],num_list[i]
#     count += 1
# 
# print(num_list)
'''

# 6.取出列表中最大的值
# 将列表[13, 20, 42, 85, 9, 45]中的最大值为85
# 提示：使用多种方法
# 方法一：使用内置函数sort
# num_list.sort(reverse = True)
# print(num_list[0])
# 方法二：使用max函数
# max(num_list)
# 方法三：使用冒泡排序
# for i in range(0,len(num_list)):
#     for j in range(i+1,len(num_list)):
#         if num_list[i] < num_list[j]:
#             num_list[i],num_list[j] = num_list[i],num_list[j]
#         else:
#             num_list[i] , num_list[j] = num_list[j] , num_list[i]
# print(num_list[-1])

# 7.编写如下程序
# a.用户输入1-7七个数字，分别代表周一到周日
# b.如果输入1~5，打印对应的“周一”~“周日”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# def days_output():
#     ''''星期输出，如果输入的为数字则对应按需输出，如果非数字则提示从新输出'''
#     num_dict = {1: "周一" , 2: "周二" , 3: "周三" , 4: "周四" , 5: "周五" , 6: "周末" , 7: "周末"}
#     while True:
#         num = int( input( "请输入数字" ) )
#         if num in num_dict.keys():
#             print( "今天是:" , num_dict[num] )
#         elif num == 0:
#             break
#         else:
#             print( "输错了,请重新输入" )
#
#
# try:
#     days_output()
# except Exception:  # 捕获异常
#     print( "只能输入数字，请重新输入" )
#     days_output()

'''
# 8.编写如下程序
# 输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
# b.根据BMI指数，给与相应提醒
# 低于18.5： 过轻
# 18.5-25：   正常
# 25-28：      过重
# 28-32：      肥胖
# 高于32：   严重肥胖

def bmi_out():
    height = float(input("请输入身高"))
    weight = float(input("请输入体重"))
    BMI = weight/(height**2)
    if BMI < 18.5:
        print("您的bmi为{:2f},过轻".format(BMI))
    elif 18.5 <= BMI < 25:
        print( "您的bmi为{:.2f},正常".format( BMI ) )
    elif 25 <= BMI < 28:
        print( "您的bmi为{:.2f},过重".format( BMI ) )
    elif 28 <= BMI <32:
        print( "您的bmi为{:.2f},肥胖".format( BMI ) )
    else:
        print( "您的bmi为{:.2f},严重肥胖".format( BMI ) )

bmi_out()
'''

'''
# 9.编写如下程序
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
# a.定义一个函数，接收用户输入的用户名和密码作为参数
# b.正确的账号，用户名为lemon，密码为best
def login():
    name = input("输入用户名：")
    password = input("请输入密码：")
    if name == "lemon" and password == "best":
        print("登陆成功")
    else:
        print("账号密码错误，请重新输入：")
        login()
login()
'''

# 11.列表去重
a = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# 方法一
new_list = []
for value in a :
    if value not in new_list:
        new_list.append(value)
print(new_list)

# 方法二   遍历列表，当列表中的某个元素个数大于1就根据这个元素的第一个匹配索引删除这个元素
for value in a:
    while a.count(value)>1:
         del a[a.index(value)]
print(a)

# 12.编写如下程序
# 打印出1-100之间除了含7和7的倍数之外的所有数字
num = []
count = 0
while count < 100:
    count += 1
    if count%7 == 0:
        continue
    elif "7" in str(count):
        continue
    else:
        num.append(count)
print(num)

# 13.编写如下程序    (此题做的有问题，需优化)
# 输入键盘数字键(0~9)，返回数字键上方字符
# a.定义如下字典num_str_dic = {'1': '!', '2': '@', '3': '#', '4': '$','5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
# b.例如：键盘输入5，程序输出%
# c.键盘输入0~9，正常输出字符之后，退出程序，否则继续提示输入
num_str_dic = {'1': '!', '2': '@', '3': '#', '4': '$','5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}


def output():
    while True:
        out = input("请输入数字")
        print(num_str_dic[out])
        del num_str_dic[out]
        print(num_str_dic)
        if len(num_str_dic) == 0:
            break
try:
    output()
except Exception:
    print("请勿重复输入")
    output()