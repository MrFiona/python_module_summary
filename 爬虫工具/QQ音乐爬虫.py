#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-06 21:31
# Author  : MrFiona
# File    : QQ音乐爬虫.py
# Software: PyCharm Community Edition


import json
import pickle
import requests
from urllib import request

response = requests.get('https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?g_tk=1831952230&jsonpCallback=MusicJsonCallbacksinger_track&loginUin=1160177283&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&singermid=003aQYLo2x8izP&order=listen&begin=0&num=30&songstatus=1')
print(response.text)

# g = open('test.json', 'wb')
# print(json.dump(response.text[31:-1], g, ensure_ascii=True, indent=4))
# g.write(response.text[31:-1])
# g.close()


# with open('test.json', 'wb') as f:
# pickle.dump(response.text[31:-1], f)
# print(json.dumps(response.text[31:-1], ensure_ascii=False, encoding='gbk'))