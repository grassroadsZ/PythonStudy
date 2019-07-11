'''
-*-conding:utf-8
@Time:2019/4/16 7:13
@auther:grassroadsZ
@file:lesson_10_0415.py
'''


# 1.什么是异常？为什么要捕获异常？
# 即便Python程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常
# 错误信息的前面部分显示了异常发生的上下文，并以调用栈的形式显示具体信息。方便找出定位问题

# 2.异常的完整语法格式
try:
    pass# 可能出现异常的代码部分
except Exception as e:
	# 这个将会捕获除了 SystemExit 、KeyboardInterrupt 和 GeneratorExit 之外的所有异常。 如果你还想捕获这三个异常，将 Exception 改成 BaseException 即可。
	print("reason", e)
else:
    pass
	# 这也是代码块
    # 一定要放在except后面
finally:
    pass
	# 无论是否有异常都会执行的部分

# 3.在异常中，try关键字下的块语句、except下的块语句、else下的块语句、finally下的块语句执行逻辑是什么？
# - 首先，执行try子句（在关键字try和关键字except之间的语句）
# - 如果没有异常发生，忽略except子句，try子句执行后结束执行else部分的语句，最后是无论如何都会执行的Finally子句。
# - 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
# - 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中


# 4.编写如下程序
# 优化去生鲜超市买橘子程序
# a.收银员输入橘子的价格，单位：元／斤
# b.收银员输入用户购买橘子的重量，单位：斤
# c.计算并且 输出 付款金额
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况

'''
def shopping():
    """
    计算用户购买橘子的总价
    :return: 输出橘子的价格，单价及最后总价
    """
    while True:
        organe_price = input( '请输入橘子价格：' )
        weight = input("您的重量为：")
        try:
            organe_price = float(organe_price)
            weight = float(weight)
            result = "橘子单价为{}元每斤，{}斤您应付：{}元".format(organe_price,weight,organe_price*weight)
            return result
        except Exception :
            print("输入有误重新输入")
shopping()
'''

# 5.编写如下程序
# 优化剪刀石头布游戏程序
# a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# b.电脑随机出拳
# c.比较胜负，显示用户胜、负还是平局
# 新需求：
# d.使用捕获异常的方式，来处理用户输入无效数据的情况
# e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平
# f.当程序结束之后，要求下一次运行程序能够获取用户历史胜负情况
# h.如果使用文件保存用户历史胜负数据，需要使用异常来处理文件不存在的情况和实现程序结束后自动关闭文件的功能（选做）

'''
import random
import time

filepath = r"F:\Python3.6\LemonPython_Study\Homework\game.txt"

def file_read(filepath = filepath, mode = "r" , encoding = 'utf-8'):
    """

    :param filepath: 文件路径
    :param mode:读取文件的方式
    :param encoding:默认编码
    :return:  游戏结果
    """
    try:
        with open( filepath , mode = mode , encoding = encoding ) as file:   # 以读模式打开文件
            file.seek(0)
            tmp_content = file.readlines()
    except Exception :  # 有异常说明文件不存在以追加模式创建然后移动指针到最前面
        result = "你没有游戏记录"
        with open( filepath , mode = 'a' , encoding = encoding ) as file:
            file.seek(0)
    else:
        if len(tmp_content) == 0:   # 判断列表为空，此处应该还可以优化，当手动删除文件里的记录时游戏运行不会输出没有游戏记录。
            result = "你没有游戏记录"
        else:
            tmp_result = tmp_content[-1]    # 读取最后一条游戏记录
            result = tmp_result.replace('当前','上次')  # 将最后一条游戏记录字符串的当前修改为上次
    print(result)

def game():
    """
    根据用户输入判断输赢并记录结果,当输入数字0时退出
    :return:
    """
    now_time = time.strftime( '%Y-%m-%d %H:%M:%S' )  # 获取当前时间格式为2019-04-16 07:49:02
    win,lose,draw = 0,0,0
    file_read()
    while True:
        user_out = input( "输入对应数字：石头(1)，剪刀(2),布(3),输入0退出" )
        try:
            user_out = int(user_out)
            if user_out == 0:
                game_result = "当前游戏时间为：{}  游戏结果为：赢{}输{}平{}".format( now_time , win , lose , draw ) + "\n"
                try:
                    # 打开文件
                    with open( filepath , 'a' , encoding = 'utf-8' ) as file:
                        file.write( str( game_result ) )
                except Exception as e:
                    print( "存在异常{}，游戏记录失败".format( e ) )
                finally:
                    print( game_result )
                    break
        except Exception:
            print("请输入数字1-3")
        else:
            computer_out = random.randint(1,3)
            if computer_out > user_out:
                lose += 1
                print("电脑赢")
            elif computer_out == user_out:
                draw += 1
                print("平局")
            else:
                win += 1
                print("用户赢")



if __name__ == '__main__':
    game()
'''