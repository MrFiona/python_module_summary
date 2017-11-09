#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-09 19:43
# Author  : MrFiona
# File    : 百度音乐爬虫.py
# Software: PyCharm Community Edition


import re
import time
import requests
from bs4 import BeautifulSoup

start_time = time.time()

# response = requests.get('http://music.baidu.com/tag')
# html = response.content.decode('utf-8')
#
# htm_soup = BeautifulSoup(html, 'html.parser')
# classify_label_list = htm_soup.select('dl[class="tag-mod"]')
# # print(classify_label_list, len(classify_label_list))
#
# try:
#
#     for classify in classify_label_list:
#         #todo 歌曲分类标签
#         # print(classify.dt)
#         # print(classify, type(classify))
#         label_a_list = classify.find_all('a')
#         #todo 歌曲分类标签下的子分类链接列表
#         classify_sep_url_list = [element.attrs['href'] for element in label_a_list]
#         label_sep_url_list = [element.string for element in label_a_list]
#         # print(label_sep_url_list)
#         # print()
#
#         for sep_url in range(len(classify_sep_url_list)):
#             response = requests.get('http://music.baidu.com/{}' .format(classify_sep_url_list[sep_url]))
#             print(u'开始解析分类歌曲链接{}' .format('http://music.baidu.com/{}' .format(label_sep_url_list[sep_url])))
#             html = response.content.decode('utf-8')
#             # print(html)
#
#             label_sep_soup = BeautifulSoup(html, 'html.parser')
#             song_label_info = label_sep_soup.select('div[monkey="song-list"]')
#             song_label_list = song_label_info[0].select('li')
#             # print(song_label_list)
#
#             for song in song_label_list:
#                 # print(song)
#                 #todo 歌曲详情子链接
#                 song_sep_link = song.select('span[class="song-title"]')[0].select('a')[0].attrs['href']
#                 #todo 歌曲作者，可能有多个作者
#                 temp = song.select('span[class="singer"]')[0].select('a')
#                 singer_list = [element.string for element in temp]
#                 #todo 专辑名称
#                 album_title = song.select('span[class="album-title"]')[0].select('a')[0].string
#                 song_name = song.select('span[class="album-title"]')[0].select('a')[0].attrs['title']
#                 print('歌曲子链接:\t', song_sep_link)
#                 print('歌曲:\t', song_name)
#                 print('歌手:\t', singer_list)
#                 print('所属专辑:\t', album_title)
#                 print()
#
#                 # http://music.baidu.com/song/564102115
#                 print(u'获取歌曲[ {} ]歌词开始.......' .format(song_name))
#                 response = requests.get('http://music.baidu.com/{}' .format(song_sep_link))
#                 html = response.content.decode('utf-8')
#
#                 #todo 获取歌词链接
#                 music_word_soup = BeautifulSoup(html, 'html.parser')
#                 m = music_word_soup.select('div[id="lyricCont"]')[0].attrs['data-lrclink']
#                 # print(m)
#                 #todo 获取歌词信息
#                 response = requests.get(m)
#                 html = response.content.decode('utf-8')
#                 # print(html.split('\n'))
#                 for word in html.split('\n'):
#                     if re.search('^\[.*\]$', word):
#                         continue
#                     # word = word.split(']')
#                     # print(word)
# except:
#     print('error')
print(time.time() - start_time)



# http://music.baidu.com/song/564102115#ucomment-bookmark
response = requests.get('http://music.baidu.com/song/564102115#ucomment-bookmarkg')
html = response.content.decode('utf-8')
# print(html)

soup = BeautifulSoup(html, 'html.parser')
print(soup.select('div[class="message-list comment-list"]'))