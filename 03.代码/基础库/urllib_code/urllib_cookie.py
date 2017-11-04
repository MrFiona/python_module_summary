#-*-coding:utf-8-*-
import urllib.request
import http.cookiejar
# 申明CookieJar对象
cj = http.cookiejar.CookieJar()
# 构建cookie处理
handler = urllib.request.HTTPCookieProcessor(cj)
# handler 来构建opener
opener=urllib.request.build_opener(handler)
urllib.request.install_opener(opener)
# open方法传入url
response=opener.open('http://www.ibeifeng.com')
for item in cj:
    print('Name:'+item.name)
    print('Value:' + item.value)
