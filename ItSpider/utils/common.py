#!/usr/bin/env python
# encoding: utf-8

"""
@author: zxj
@contact: 165390188@qq.com
@time: 2018/10/25/025 18:22
"""
import hashlib

def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()