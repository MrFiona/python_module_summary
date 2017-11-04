#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-04 18:22
# Author  : MrFiona
# File    : BeautifulSoup功能总结.py
# Software: PyCharm Community Edition


import re
import codecs
from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" id="213123"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister1" href="http://example.com/elsie" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister2" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister3" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# html = codecs.open('5702_Gold.html', encoding='utf-8')
# print(html.read())
#todo 加载html代码，返回一个BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.find_all('p')
print(result, len(result))
print()

#todo ****************************1、获取节点****************************

#todo (1)、获取第一个出现的指定节点
print(soup.p)  #获取soup对象中第一个出现的p标签子节点

#todo (2)、获取所有的指定节点 返回子节点列表
print(soup.find_all('p')) #或者也可以soup.contents来获取

#todo (3)、通过contents获取子节点 返回子节点列表  .contents 和 .children 属性仅包含tag的直接子节点.例如,<head>标签只有一个直接子节点<title>
#todo 但是<title>标签也包含一个子节点:字符串 “The Dormouse’s story”,这种情况下字符串 “The Dormouse’s story”也属于<head>标签的子孙节点.
#todo .descendants 属性可以对所有tag的子孙节点进行递归循环
print(soup.p.contents) #获取p节点的子节点b
print(result[0].contents) #再次获取p子节点b节点的子节点
#todo 注意：字符串没有子节点

#todo (4)、通过children获取子节点 返回包含子节点信息的迭代器
print('children:\t', list(soup.children))

#todo (5)、通过descendants获取子节点 返回包含子孙节点信息的迭代器  子孙节点信息嵌套在一起，不太容易看
print('descentants:\t', list(soup.descendants))

#todo (6)、通过.parent获取父节点
p = soup.p
print('p parent:\t', p.parent, type(p.parent))
html = soup.html
#todo 文档的顶层节点<html>的父节点是BeautifulSoup对象；BeautifulSoup对象的parent是None
print('html parent:\t', html.parent, type(html.parent))
print('soup parent:\t', soup.parent, type(soup.parent))

#todo (7)、通过.next_sibling 和 .previous_sibling获取兄弟节点  这里的同级是非本身的其他节点，例如soup.a.previous_sibling是同一个父节点并且与a节点同级而不是a节点的节点
print('\033[35mnext_sibling:\t\033[0m', soup.a.previous_sibling)
print()

#todo ****************************1、获取节点****************************


#todo ****************************2、获取节点的属性****************************

#todo (1)、获取某个属性 返回属性值列表
print(soup.p['class'])

#todo (2)、获取所有的属性 结果是属性key-value字典，value是个列表，其中的元素是属性值
print(soup.p.attrs)

#todo (3)、获取节点的名称
print(soup.p.name)
print()

#todo ****************************2、获取节点的属性****************************


#todo ****************************3、获取节点的字符串****************************

#todo (1)、如果tag只有一个子节点,那么这个tag可以使用 .string 得到子节点
print(soup.p.string)

#todo (2)、如果tag包含了多个子节点，则使用.strings，如果使用.string那么它会因为不知道调用哪个节点而导致返回None
print(list(soup.strings))
print(soup.string) #多个节点的情况下调用.string会导致 返回None
#todo 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容  全部是空格的行会被忽略掉,段首和段末的空白会被删除
print(list(soup.stripped_strings))
#todo 获取第一个title标签的对应内容
print (soup.select('title')[0].get_text())
print()

#todo ****************************3、获取节点的字符串****************************


#todo ****************************4、find_all()方法****************************

#find_all(self, name=None, attrs={}, recursive=True, text=None,limit=None, **kwargs)
"""
        soup.find_all('b')  #查找所有的b标签，返回列表
        soup.find_all(re.compile("^b")) # 正则表达式
        soup.find_all(["a", "b"])  #传入列表参数，找到所有的a标签和b标签
        soup.find_all(id='link2')  #传入id是link2的参数,Beautiful Soup会搜索每个tag的”id”属性
        soup.find_all(href=re.compile("elsie")) #传入正则表达式，查找所有的href标签内容中含有 elsie 的内容
        soup.find_all(href=re.compile("elsie"), id='link1') # 多层过滤，除了href进行限定之外，对id标签的内容也做了限定
        soup.find_all("div", class_="sister") #最常用的查找技巧，这里之所以加‘_=’是因为‘class’不仅是html中的tag，也是python语法的关键词，其他的不用加下划线
        data_soup.find_all(attrs={"data-foo": "value"}) # 针对html5里面的data- 进行的专项查找
        soup.find_all(text="Elsie") # 对text内容进行查找
        soup.find_all(text=["Tillie", "Elsie", "Lacie"]) # 列表形式进行查找，与上面name类似
        soup.find_all(text=re.compile("Dormouse")) # 正则表达式形式，与上面类似
        soup.find_all("a", limit=2) # 找到前两个a标签， limit用来限定次数(

"""

print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
print(soup.find_all(text=re.compile("Dormouse")))
print(soup.find_all("a", limit=2))
print(soup.find_all(["a", "b"]))
print(soup.find_all("a", class_="sister3"))

#todo ****************************4、find_all()方法****************************

# for tr in result:
#     string_list = list(tr.strings)
#     string_list = [ele.replace('\\n', '') for ele in string_list]
#     string_list = [ele for ele in string_list if not ele.isspace()]
#     string_list = [ele for ele in string_list if len(ele)]
#     print(string_list)

#todo ****************************5、select()方法****************************

#todo （1）通过标签名查找
print('seclect:\t', soup.select('title'))
#todo （2）通过类名查找
print(soup.select('.story'))
#todo （3）通过 id 名查找
print(soup.select('#213123'))
#todo （4）组合查找
print(soup.select('p #link1'))

#todo ****************************5、select()方法****************************
