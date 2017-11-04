#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-04 23:33
# Author  : MrFiona
# File    : lxml功能总结.py
# Software: PyCharm Community Edition


from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
</div>
'''


html = etree.HTML(text)
# html = etree.parse(text)
result = etree.tostring(html)
print(result)

result = html.xpath('//li')
print(result, type(result), len(result))

for ele in result:
    print(dir(ele))
    print(ele.values)

result = html.xpath('//li/@class')
print(result, type(result), len(result))

for ele in result:
    print(ele)
