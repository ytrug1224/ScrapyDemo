#!/usr/bin/env python
# encoding: utf-8

import requests


def handle_request(url, data):
    header = {
        "imei": "863254011122123",
        "channel": "360box",
        # "mac": "50:7B:9D:39:7E:4E",
        "resolution": "1920*1080",
        "dpi": "2.0",
        # "android-id": "17a0cb8e1647d454",
        # "pseudo-id": "b8e1647d45417a0c",
        "brand": "Xiaomi",
        "scale": "2.0",
        "timezone": "28800",
        "language": "zh",
        "cns": "3",
        "carrier": "CHINA+MOBILE",
        # "imsi": "460071122121842",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 6  Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36",
        "reach": "1",
        "newbie": "0",
        # "lon": "105.566938",
        # "lat": "29.99831",
        # "cid": "512000",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        # "Cookie": "duid=58465974",
        "Host": "api.douguo.net",
        # "Content-Length": "89",
    }
    return requests.post(url=url, headers=header, data=data)


def request_url():
    url = "http://api.douguo.net/recipe/flatcatalogs"
    data = {
        "client": 4,
        # "_session": "1547801881859863254011122123",
        # "v": "1503650468",
        "_vs": "2305"
    }

    response = handle_request(url=url, data=data)
    print(response.text)


request_url()
