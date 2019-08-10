"""
-*-conding: utf-8
@Time:2019-06-15 7:37
@Auther:grassroadsZ
@File:handle_webservice.py
"""

from json import loads
from suds.client import Client


class WebService:
    """
    定义封装后的webservice请求
    """
    def __call__(self, url, api, data=None, is_json=False, **kwargs):
        """
        :param url:请求uri
        :param api: 接口请求地址
        :param data: 传参
        :param is_json: True/False
        :param kwargs: 请求响应信息
        :return:
        """
        if isinstance(data, str):
            try:
                data = loads(data)
            except Exception as e:
                print(e)
                data = eval(data)
        self.client = Client(url).service
        send_api = getattr(self.client, api)
        try:
            res = send_api(data)
        except Exception as e:
            res = e.fault
            return res
        else:
            return res


if __name__ == '__main__':
    web = WebService()
    t = {"tmpl_id": 1, "client_ip": "129.45.6.7", "mobile": "13921212111"}
    # print(web(url, "sendMCode", t))
