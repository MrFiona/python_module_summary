#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-01 19:44
# Author  : MrFiona
# File    : test_1.py
# Software: PyCharm Community Edition


from pandas import Series, DataFrame
import pandas as pd


read_data =pd.read_csv('ca_list_copy(2).csv', delimiter=',')
print type(read_data)

# print read_data.columns

# for col in read_data.columns:
#     print '%s:\t' % col, read_data[read_data[col] == 0], type(read_data[read_data[col] == 0])
#     read_data.replace(0, 9999)

print read_data[read_data['zwyx'] == 0]
read_data['zwyx'] = read_data['zwyx'].replace(0, read_data['zwyx'].mean())
# read_data['zwyx'][read_data['zwyx'] == 0][1] = 10000.0
# print type(read_data['zwyx'])
# print read_data['zwyx']
# print read_data['zwyx'][read_data['zwyx'] == 11111111]
# print read_data
print read_data[read_data['zwyx'] >= 8152.994976]
# print '1111:\t', read_data[read_data != 0]