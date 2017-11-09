import requests
import urllib
import json
from urllib import parse

#缺少对于歌名的相关信息的获取
# 歌曲分类，歌词，风格，其他歌名
#1.抓取所有的分类的id，然后拼接出对应的分类的链接
#2.访问分类的链接，抓取所有歌单的详细页面的链接
#3.访问详细页面的链接，抓取所有歌曲的详细页面的链接
#4.抓取歌曲的信息
headers={
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'cookie':'pgv_pvi=4233738240; pgv_pvid=5690977260; yq_index=0; pgv_si=s6751886336; ts_last=y.qq.com/; ts_uid=4339540520; yqq_stat=0',
'referer':'https://y.qq.com/portal/playlist.html',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
}
#1.传入处理好的分类歌单的链接，抓取所有歌单的详细页面的链接
def get_song_list(url=''):
    if not url:
        url= 'https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd=0.03505015454872451&g_tk=5381&jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5&sin=0&ein=29'
    # 1.访问分类歌单的页面，进行页面解析
    html = requests.get(url,headers=headers).text
    getPlaylistTags = json.loads(html.strip('getPlaylist(').strip(')'))
    # 获取data_id 的值
    url_list = []
    for item in getPlaylistTags['data']['list']:
        url = 'https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid={0}&format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'.format(item['dissid'])
        url_list.append(url)
            #  拼接下一页的链接
    if getPlaylistTags['data']['ein'] < getPlaylistTags['data']['sum']:
        next_page = "https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd=0.03505015454872451&g_tk=5381&jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5&sin={0}&ein={1}".format(getPlaylistTags['data']['sin'] + 30,getPlaylistTags['data']['ein'] + 30)
    else:
        next_page = ''
    return url_list, next_page

#3.访问详细页面的链接，抓取所有歌曲的详细页面的链接
def get_info_list(url):
    print(parse.urlparse(url))
    headers['referer']='https://y.qq.com/n/yqq/playlist/'+parse.urlparse(url)['dissid']+'.html'
    html=requests.get(url,headers=headers).text
    playlistinfoCallback=json.loads(html.strip('playlistinfoCallback(').strip(')'))
    song_list=[]
    albummid=[]
    for item in playlistinfoCallback['cdlist'][0]['songlist']:
        song_list.append('https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?songmid=003cOQUV2AvE5A&tpl=yqq_song_detail&format=jsonp&callback=getOneSongInfoCallback&g_tk=5381&jsonpCallback=getOneSongInfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'.format(item['songmid']))
        albummid.append(
            'https://c.y.qq.com/v8/fcg-bin/fcg_v8_album_info_cp.fcg?albummid={0}&g_tk=5381&jsonpCallback=getAlbumInfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'.format(
                item['albummid']))
    return song_list,albummid
#4.抓取歌曲的信息
def get_info_content(song_url,albummid_url):
    html = requests.get(song_url).text
    getOneSongInfoCallback = json.loads(html.strip('getOneSongInfoCallback(').strip(')'))
    getAlbumInfoCallback=json.loads(requests.get(albummid_url).text.strip('getAlbumInfoCallback(').strip(')'))
    song_dict={}
    song_dict['songName']=getOneSongInfoCallback['data'][0]['name']
    song_dict['singerName']=getOneSongInfoCallback['data'][0]['singer'][0]['name']
    song_dict['time_public']=getOneSongInfoCallback['data'][0]['time_public']
    genre=getAlbumInfoCallback['data']['genre']
    lan=getAlbumInfoCallback['data']['lan']

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


info_urls=[]
ulrs,next_page=get_song_list()
info_urls.extend(ulrs)
while next_page:
    ulrs, next_page = get_song_list(next_page)
    info_urls.extend(ulrs)
#3->4
for info_url in info_urls:
    print(info_url)
    #info_content_url = get_info_list(info_url)
    #print(info_content_url)
    # for content_url in info_content_url:
    #     print(content_url)
    #     get_info_content(content_url, item['name'])
