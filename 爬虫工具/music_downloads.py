#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib
import json
from urllib import parse

#缺少对于歌名的相关信息的获取
# 歌曲分类，歌词，风格，其他歌名
#1.抓取所有的分类的id，然后拼接出对应的分类的链接
#2.访问分类的链接，抓取所有歌单的详细页面的链接
#3.访问详细页面的链接，抓取所有歌曲的详细页面的链接
#4.抓取歌曲的信息，并将歌曲名传递给download_music实现，下载对应音乐文件


def download_music(word):
    #如下的代码完成了音乐文件的下载
    #word = '彩虹'
    res1 = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w='+word)
    jm1 = json.loads(res1.text.strip('callback()[]'))
    jm1 = jm1['data']['song']['list']
    mids = []
    songmids = []
    srcs = []
    songnames = []
    singers = []
    for j in jm1:
        try:
            mids.append(j['media_mid'])
            songmids.append(j['songmid'])
            songnames.append(j['songname'])
            singers.append(j['singer'][0]['name'])
        except:
            print('wrong')


    for n in range(0,len(mids)):
        res2 = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid='+songmids[n]+'&filename=C400'+mids[n]+'.m4a&guid=6612300644')
        jm2 = json.loads(res2.text)
        vkey = jm2['data']['items'][0]['vkey']
        srcs.append('http://dl.stream.qqmusic.qq.com/C400'+mids[n]+'.m4a?vkey='+vkey+'&guid=6612300644&uin=0&fromtag=66')

    print('For '+word+' Start download...')
    x = len(srcs)
    for m in range(0,x):
        print(str(m)+'***** '+songnames[m]+' - '+singers[m]+'.mp3 *****'+' Downloading...')
        try:
            urllib.request.urlretrieve(srcs[m],'music/'+songnames[m]+' - '+singers[m]+'.mp3')
        except:
            x = x - 1
            print('Download wrong~')
    print('For ['+word+'] Download complete '+str(x)+'files !')



