#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-09 19:43
# Author  : MrFiona
# File    : 百度音乐爬虫.py
# Software: PyCharm Community Edition


import re
import time
import json
import requests
import pandas as pd
import numpy as np
from lxml import etree
from bs4 import BeautifulSoup

start_time = time.time()

#todo 歌曲总分类标签以及链接信息
global_music_classify_label_info = {}


response = requests.get('http://music.baidu.com/tag')
html = response.content.decode('utf-8')

htm_soup = BeautifulSoup(html, 'html.parser')
classify_label_list = htm_soup.select('dl[class="tag-mod"]')
# print(classify_label_list, len(classify_label_list))
for element in classify_label_list:
    label_name = element.find_all('dt')[0].string
    classify_object_list = element.select('span[class="tag-list clearfix"]')
    classify_music_link_info = { link.a.string : ''.join(['http://music.baidu.com', link.a.attrs['href']]) for link in classify_object_list }
    # print('%s歌曲分类链接:\t' % label_name, classify_music_link_info)
    global_music_classify_label_info[label_name] = classify_music_link_info

# print(global_music_classify_label_info)

df = pd.DataFrame([], columns=['date','aa', 'bb', 'cc'],index=[])
new= pd.DataFrame({"aa":10,"bb":"b1","cc":20},index=[1])
df = df.append(new)
print(df)
try:
    for classify in global_music_classify_label_info:
        try:
            print(u'\033[32m开始下载总分类为 [{0}] 的歌曲\033[0m' .format(classify))
            for child_classify in global_music_classify_label_info[classify]:
                try:
                    print(u'\033[33m开始下载子分类为 [{0}] 的歌曲\033[0m' .format(child_classify))
                    cycle_recursive_flag = True
                    cycle_url = global_music_classify_label_info[classify][child_classify]
                    page_num = 1
                    df = pd.DataFrame([], columns=[u'歌手', u'专辑', u'歌曲', u'发行时间', u'发行公司', u'歌词文件下载链接', u'总分类', u'子分类', u'页数'], index=[])
                    while cycle_recursive_flag:
                        print(u'开始爬取子分类 [{0}] 第 [{1}] 页的歌单' .format(child_classify, page_num))
                        time.sleep(4)
                        child_classify_response = requests.get(cycle_url)
                        child_classify_html = child_classify_response.content.decode('utf-8')
                        # print(child_classify_html)
                        #todo 歌曲分类标签
                        child_classify_soup = etree.HTML(child_classify_html)
                        label_a_list = child_classify_soup.xpath('//div[@class="main-body"]/div[@class="main-body-cont"]/div[@class="tag-main"]/div[@monkey="song-list"]/ul/li')
                        #todo 获取分类下的所有歌曲信息 会有50页歌单，每页20首歌曲
                        for music in label_a_list:
                            music_info = music.attrib[u'data-songitem']
                            json_music_info = json.loads(music_info)[u'songItem']
                            # print(json_music_info)
                            #todo 歌曲名称
                            music_name = json_music_info[u'author']
                            print(u'歌曲名称:\t', music_name)
                            #todo 歌手
                            singer_name = json_music_info[u'sname']
                            print(u'歌手名称:\t', singer_name)

                            #todo 获取歌词，专辑信息
                            #todo 获取链接
                            other_info_link = ''.join([u'http://music.baidu.com/song/',json_music_info[u'sid']])
                            print(u'歌词，专辑信息链接', other_info_link)

                            other_html = requests.get(other_info_link).content.decode('utf-8')
                            other_soup = BeautifulSoup(other_html, 'html.parser')
                            try:
                                #todo 歌曲专辑
                                album = other_soup.select('div[class="song-info"]')[0].select('div[class="song-info-box"]')[0].select('div[class="info-holder clearfix"]')[0].find_all('li', class_='clearfix')[0].a.stripped_strings
                                album = list(album)[0]
                                print(u'歌曲专辑:\t', album)
                            except:
                                print(u'歌曲 [ {0} ] 获取专辑失败，获取专辑的链接为 [ {1} ]' .format(music_name, other_info_link))

                            #todo 获取歌词链接
                            try:
                                m = other_soup.select('div[id="lyricCont"]')[0].attrs['data-lrclink']
                                #todo 获取歌词信息
                                response = requests.get(m)
                                html = response.content.decode('utf-8')
                                for word in html.split('\n'):
                                    if re.search('^\[.*\]$', word):
                                        continue
                                    try:
                                        word = word.split(']')[1]
                                        print(word)
                                    except:
                                        pass
                            except IndexError:
                                print(u'歌曲 [ {0} ] 无歌词，获取歌词的链接为 [ {1} ]' .format(music_name, m))

                            try:
                                #todo 获取发行时间以及发行公司
                                publish_sep_link = other_soup.select('div[class="song-info"]')[0].select('div[class="song-info-box"]')[0].select('div[class="info-holder clearfix"]')[0].find_all('li', class_='clearfix')[0].a['href']
                                publish_info_link = ''.join([u'http://music.baidu.com', publish_sep_link])
                                print(u'发行时间以及发行公司链接:\t', publish_info_link)
                                publish_info_html = requests.get(publish_info_link).content.decode('utf-8')
                                publish_info_html = publish_info_html.replace('&nbsp;', '')
                                publish_soup = BeautifulSoup(publish_info_html, 'html.parser')
                                publish_info = publish_soup.find_all('ul', class_="c6")[0].find_all('li')[-2].string
                                #todo 发行时间
                                publish_info = re.split('\s{2,}', publish_info)
                                #todo 以分号分隔,\uff1a为：的unicode编码
                                publish_time = publish_info[0].split(u'\uff1a')[1].strip()
                                #todo 发行公司
                                publish_company = publish_info[1].split(u'\uff1a')[1].strip()
                                print(u'发行时间:\t', publish_time)
                                print(u'发行公司:\t', publish_company)

                            except:
                                print(u'歌曲 [ {0} ] 获取发行时间以及发行公司失败!!!，获取歌词的链接为 [ {1} ]' .format(music_name, publish_info_link))

                            new = pd.DataFrame({u'歌手': singer_name, u'专辑': album, u'歌曲': music_name, u'发行时间': publish_time, u'发行公司': publish_company,
                                                u'歌词链接': m, u'总分类': classify, u'子分类': child_classify, u'页数': page_num}, index=[u"{0}" .format(str(page_num))])
                            df = df.append(new)
                            # print(df)

                        # df2 = pd.read_csv(u'{0}_{1}_{2}.csv'.format(classify, child_classify, page_num), encoding="utf-8")
                        # print('wwwww:\t', df2)

                        #todo 获取下一页链接
                        try:
                            next_page_link = child_classify_soup.xpath('//div[@class="page-cont"]/div[@class="page-inner"]/a[@class="page-navigator-next"]')[0].attrib[u'href']
                            cycle_url = ''.join([u'http://music.baidu.com', next_page_link.strip()])
                            print(u'下一页歌曲链接:\t', cycle_url)
                        except:
                            print(u'\033[35m爬取子分类为 [{0}]的歌曲结束，一共 [{1}] 页歌单\033[0m' .format(child_classify, page_num))
                            cycle_recursive_flag = False

                        page_num += 1
                    df.to_csv('{0}_{1}.csv'.format(classify, child_classify), encoding='utf_8_sig')
                except:
                    pass
        except:
            pass

except:
    print('error')

print(time.time() - start_time)