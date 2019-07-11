'''
-*-conding:utf-8
@Time:2019-05-26 20:53
@auther:grassroadsZ
@file:lesson_22_0524.py
'''
import json
import requests

url = "http://120.78.128.25:8080/futureloan/mvc/api/"
def request_base(address):
    return "/".join([url,address])

def zhuce():
    # 读取单json文件当做参数传参
    with open(r"F:\Python3.6\LemonPython_Study\Homework\lesson_21_0520_fina_rewrite\test_json.txt",encoding = "utf-8") as f:
        data = json.load(f)
        # print(type(json.d))
    response = requests.post(request_base("member/register"),data = data)
    response_dict = json.loads(response.text)
    print(response_dict,type(response_dict))
    # 将响应的单json信息写入到文件中
    with open(r"F:\Python3.6\LemonPython_Study\Homework\lesson_21_0520_fina_rewrite\test_json1.txt",mode = "a",encoding = "utf-8") as f1:
        json.dump(response_dict,f1)

    # 读取多个json的文件列表应该是文件写的有问题
    # with open(r"F:\Python3.6\LemonPython_Study\Homework\lesson_21_0520_fina_rewrite\test_json_dict.txt",encoding = "utf-8") as f2:
    #     data_file= json.loads(f2)
    #     print(type(data_file))


zhuce()
