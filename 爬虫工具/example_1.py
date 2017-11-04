#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-04 09:35
# Author  : MrFiona
# File    : example_1.py
# Software: PyCharm Community Edition


from bs4 import BeautifulSoup

from urllib import request


httpHandler = request.HTTPHandler(debuglevel=1)
httpHandler1 = request.HTTPSHandler(debuglevel=1)
opener = request.build_opener(httpHandler1, httpHandler)
request.install_opener(opener)
request1 = request.Request('http://www.ibeifeng.com')
response = request.urlopen(request1)
print(response)
# print(response.read().decode('gbk'))