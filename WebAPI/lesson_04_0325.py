#-*-conding:utf-8
#@Time:2019/3/26 12:46
#@auther:grassroadsZ
#@file:lesson_04_0325.py

'''
# 2.请写出if判断语句的格式
a = int(input("输入数字："))
if a == 1:
    print("1")
elif a == 2:
    print("2")
else:
    print("其它")
'''

'''
# 3.求三个整数中的最大值
# 提示：三个整数使用input提示用户输入
# 先定义一个空列表，将三次的值添加到空列表中后从小到大排序
# 方法一：
num_list = []
num1 = int(input("请输入第一个数："))
num_list.append(num1)

num2 = int(input("请输入第二个数："))
num_list.append(num2)

num3 = int(input("请输入第三个数："))
num_list.append(num3)

num_list.sort() # 从小到大排序
print(num_list[-1])

# 方法二：
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
c = int(input("请输入第三个数字："))
if a > b:
    max_num = a
    if a > c:
        max_num = a
else:
    max_num = b
    if b > c :
        max_num = b
    else:
        max_num = c
print("最大的值为：",max_num)
'''

'''
# 4.判断是否为闰年
# 输入一个有效的年份（如：2019），判断是否为闰年
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”

year = int(input("请输入一个年份："))
if year%4 == 0 and year%400 != 0:   # 能被4整除但不能被400整除的年份为普通闰年
    print("{:d}是普通闰年".format(year))
elif year%400 == 0:                 # 能被400整除的为世纪闰年
        print("{:d}是世纪闰年".format(year))
else:
    print("{:d}不是闰年".format(year))
'''


# 5.分别使用for和while打印九九乘法表(此处输出打印有问题)
for i in range(1,10):
    for j in range(1,i+1):
        print( "{}*{}={}".format( i , j , i * j ) , end = "\t" )
    print( "\t" )

# while 循环九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i :
#         print(i,"*",j,"=",i*j,end ="\t" )
#         j += 1
#     i += 1
#     print( "\t" )




'''
# 6.思维导图
# http://naotu.baidu.com/file/9496bf39247484fecaa60bc4d2510b99?token=f889bb3520597ce1
'''

'''
# 7.使用if语句完成剪刀石头布游戏
# 提示：
# 提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 电脑随机出拳
# 比较胜负，显示用户胜、负还是平局
# 使用随机数，首先需要导入随机数的模块 —— “工具包”
# import random
import random
computer_out = random.randint(1,3)
compoter_out = int(input("输入对应数字：石头(1)，剪刀(2),布(3):"))
if computer_out > compoter_out:
    print("电脑赢")
elif computer_out == compoter_out:
    print("平局")
else:
    print("用户赢")
'''

'''
# 8.使用循环实现经典冒泡算法
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
a=[1,7,4,89,34,2]
for i in range(0,len(a)) :  # 遍历元素
    for j in range(i+1,len(a)): # 遍历元素+1的元素
        if a[j] < a[i] :    # 如果元素+1的元素小于元素，则两个元素位置互换。
            a[i],a[j] = a[j],a[i]
print(a)
'''
