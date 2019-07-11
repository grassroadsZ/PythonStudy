'''
-*-conding:utf-8
@Time:2019/4/13 12:54
@auther:grassroadsZ
@file:lesson_09_0412.py
'''
'''
#
# 1.什么是文件？有哪些种类？
# 文件是一存储在硬盘里的一系列的0和1，种类有文字，图片，视频，音乐等
#
# 2.文件的操作步骤
#打开：file = open()
#操作：file.read()
#       file.write()
#       file.append()
#关闭：file.close()
# 3.操作文件的常用函数/方法有哪些？
# file.seek()			# 指定文件指针的位置
# file.tell()			# 返回文件当前位置
# r以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# w打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# 当需要使用二进制方式打开时需要加b
# 4.read、readline、readlines有什么区别？

#file.read()			# 一次性读取全部文件
# file.readline()		# 一次读取一行文件
# file.readlines()	# 读取全部文件，将文件每行作为一个列表中的元素返回一个列表


# 提示：请从返回的对象类型、文件指针位置、应用场景来阐述
# 5. 打开文件的方式有哪些？
# r以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# w打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# 当需要使用二进制方式打开时需要加b

# 6.编写如下程序
# 将你喜欢的一首歌（音乐文件拓展名为mp3，比如刘德华忘情水.mp3），通过文件读写的方法将其复制，并修改文件名

# 打开
file = open(r'F:\Python3.6\LemonPython_Study\Homework\沙漠骆驼.mp3',mode = 'rb')
file_copy = open(r"F:\Python3.6\LemonPython_Study\Homework\沙漠骆驼copy.mp3",mode = 'wb')
# 操作
file_content = file.read()
file_copy_content = file_copy.write(file_content)
# 关闭
file.close()
file_copy.close()
'''
# 7.编写如下程序
# 有两行数据，存放在txt文件里面：
# url:http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
# 请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
# [{'url':'http://test.lemonban.com/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},
# {'url':'http://test.lemonban.com/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！

'''
def file_operate():
    """
    使用for循环逐行遍历文件，将每行的文件进行两次切割每行的内容组成一个字典，返回一个由每行字典组成的列表
    :return:
    """
    file = open('F:\Python3.6\LemonPython_Study\Homework\\url.txt',mode = 'r',encoding = 'utf-8')
    dict1={}
    dict2 ={}
    for a in file:
        a = file.readline().split('@')  # 第一次切片得出列表
        for i in a:     # 列表遍历第二次切片
            k = i.split(':',1)
            for j in k:     # 遍历两次切片后的列表取key和value
                dict1[k[0]] = k[1]
                dict2[k[0]] = k[1]
    list1 = [dict1,dict2]
    return list1
'''

# 9.编写如下程序
# 创建一个txt文本文件，以csv格式（数据之间以英文逗号分隔）来添加数据
# a.第一行添加如下内容：
# name,age,gender,hobby,motto
# b.从第二行开始，每行添加具体信息，例如：
# 可优,17,男,臭美,Always Be Coding!
# 柠檬小姐姐,16,女,可优,Lemon is best!
# c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：
# person_info = [{"name": "可优",
#                "age": 17,
#                "gender": "男",
#                "hobby": "臭美",
#                "motto": "Always Be Coding!"},
#               {"name": "柠檬小姐姐",
#                "age": 16,
#                "gender": "女",
#                "hobby": "可优",
#                "motto": "Lemon is best!"},
#               ]
# d.将所有用户信息写入到txt文件中之后，然后再读出
# e.有精力的同学可以试试，多种方法来读取文件，比如csv模块（不作要求）
# 注意：csv格式的数据，是以英文逗号分隔的

def person_info(**info):
    """
    根据输入读取person_info
    :return:
    """
    file_info = open(r'F:\Python3.6\LemonPython_Study\Homework\info.txt',mode = 'a',encoding = "utf-8")


person_info(name='ceshi',age='10',gender='man',hobby='chi',motto='123')