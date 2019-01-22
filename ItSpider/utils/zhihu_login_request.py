#!/usr/bin/env python
# encoding: utf-8

"""
@author: zxj
@contact: 165390188@qq.com
@time: 2018/10/30/030 12:06
"""

import requests
import re
try:
    import cookielib
except:
    import http.cookiejar as cookielib

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未能加载")

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
header = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhizhu.com",
    'User-Agent': agent
}


def get_xsrf():
    response = requests.get("https://www.zhihu.com", headers=header)
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text, re.DOTALL)
    if match_obj:
        print(match_obj.group(1))

    return ""


def zhihu_login(account, password):
    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/api/v3/oauth/sign_in"
        post_data = {
            "_xsrf": "",
            "username":""
        }


get_xsrf()
