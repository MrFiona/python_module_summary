#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-05 22:20
# Author  : MrFiona
# File    : 豆瓣top250.py
# Software: PyCharm Community Edition


import time
import requests
from lxml import etree

start = time.time()

response = requests.get('https://www.douban.com/doulist/3936288/')
html = response.text

html_doc =  etree.HTML(html)
print(html_doc)

movie_info_object = html_doc.xpath('//div[@id="wrapper"]/div[@id="content"]')[0]
print(movie_info_object)

#todo 提取豆瓣电影TOP250标题
movie_title = movie_info_object.xpath('//h1/text()')[0]
print(movie_title)

#todo 获取25部电影信息的对象
movie_signal_object_list = movie_info_object.xpath('//div[@class="doulist-item"]//div[@class="title"]/a[@href]')
print(movie_signal_object_list, len(movie_signal_object_list))

#todo 获取电影链接列表
movie_signal_object_list = [element.values()[0] for element in  movie_signal_object_list]
print(movie_signal_object_list, len(movie_signal_object_list))

# print(dir(movie_signal_object_list[0]))
# print(movie_signal_object_list[0].values())
# print(movie_signal_object_list[0].items())
for movie in movie_signal_object_list:
    signal_movie_html = requests.get(movie).text
    signal_movie_html_doc = etree.HTML(signal_movie_html)

    try:
        #todo 获取电影名称
        movie_name_info = signal_movie_html_doc.xpath('//div[@id="content"]/h1/span/text()')

        print('movie_name:\t', ' '.join(movie_name_info))
        #todo 获取电影导演、编剧、主演信息
        movie_director = signal_movie_html_doc.xpath('//div[@class="subject clearfix"]//div[@id="info"]//span[@class="attrs"]/a[@rel="v:directedBy"]/text()')
        movie_star = signal_movie_html_doc.xpath('//div[@class="subject clearfix"]//div[@id="info"]//a[@rel="v:starring"]//text()')
        info = signal_movie_html_doc.xpath('//div[@class="subject clearfix"]//div[@id="info"]//span[@class="attrs"]')
        # movie_director = info_1[0].xpath('/a/text()')
        movie_screenwriter = info[1].xpath('/a/text()')
        # movie_star = info_1[2].xpath('//a/text()')
        print('movie_director:\t', movie_director)
        print('movie_screenwriter:\t', movie_screenwriter, len(movie_screenwriter))
        print('movie_star:\t', movie_star, len(movie_star))
    except IndexError as e:
        #todo 电影详情页面不存在
        print(e.message)

print(time.time() - start)