#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-04-05 21:30
# Author  : MrFiona
# File    : search_telnum_and_idcard.py
# Software: PyCharm

import re

uq = "手机号码为18921139662, 身份证号码为342222189808061635，号码17032345821"
# 中国移动 134-139,147,150-152,157-159,178,182-184,187,188,172 子号段
# 中国联通 130-132,145,155,156,175,176,185,186 子号段
# 中国电信 133,149,153,173,177,180,181,189 子号段
# 虚拟运营商：1703|1705|1706(移动),1704|1707|1708|1709|171(联通),1700|1701|1702
regex_telephone = '^.*[^0-9]((((13[4-9]|147|15[0-2|7-9]|17[2|8]|18[2-4|7-8])|(13[0-2]|14[4-5]|15[5-6]|17[5-6]|18[5-6])|(133|149|153|17[3|7]|18[0-1|9]))\d{8})|(170[0-9]\d{7}))\\b'
regex_id = '^.*[^0-9]((1[1-5]|2[1-3]|3[1-7]|4[1-6]|5[0-4]|6[1-5]|8[1-2])(\d{8})(0[1-9]|1[1-2])(0[1-9]|[1|2][1-9]|3[0-1])(\d{3})(\d|X))\\b.*$'
# 匹配多个手机号码以及身份证，去重
# word_split = re.split('\D+',uq)
# print(word_split)

tel_obj = re.search(regex_telephone, uq)
id_obj = re.search(regex_id, uq)
# print(tel_obj)
if tel_obj:
    print(tel_obj.groups())

# print(id_obj)
if id_obj:
    print(id_obj.groups())


# test_word = 'chapter'
# print(re.search(r'ter\b',test_word))