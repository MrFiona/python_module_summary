from lxml import etree
import requests
def get_list(go_url='https://www.cnblogs.com/'):
    html=requests.get(go_url).text
    sel=etree.HTML(html)
    #获取文章详细页面链接
    href=sel.xpath('//*[@id="post_list"]/div/div/h3/a/@href')
    #获取下一页链接
    next_page=sel.xpath('//*[@id="paging_block"]/div/a[last()]/@href')
    print(next_page)
    return href,next_page

#访问文章详细信息，获取文章的详细内容，存储到一个列表里
def get_info(url,save_list):
    html = requests.get(url).text
    sel = etree.HTML(html)
    title=sel.xpath('//*[@id="cb_post_title_url"]/text()')[0]
    content=sel.xpath('string(//*[@id="cnblogs_post_body"])')
    save_dict={}
    save_dict['title']=title
    save_dict['content']=content
    save_list.append(save_dict)

urls_list=[]
urls, next_url = get_list()
urls_list.extend(urls)
while True:
    if next_url:
        urls, next_url=get_list('http://www.cnblogs.com'+next_url[0])
    else:
        break
save_list=[]
for url in urls_list:
    get_info(url,save_list)

import pandas as pd
save = pd.DataFrame(save_list)
print(save)
# save.to_csv('b.csv',index=False,sep='')
