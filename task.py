#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-03-14 22:39
# Author  : MrFiona
# File    : task.py
# Software: PyCharm




import time
import numpy as np
import pandas as pd
import warnings
from collections import OrderedDict


start = time.time()
warnings.filterwarnings('ignore')

# df = pd.read_excel('zhangpeng_head.xlsx')
# print(df)
# print(dir(df))
# print(df.keys())
#
#
# column_list = ['标准问题', '测试样例', '维度', '标准答案']
# result_df = pd.DataFrame(columns=df.keys())
#
#
# for index in df.keys():
#     result_df[index] = getattr(df, index)
#
#
# result_df.to_csv('result.csv', encoding='gb18030', index=False)


df = pd.read_csv('result.csv', encoding='gb18030')
# print(df)
# print(df.columns)
original_columns = df.columns
print(original_columns, len(original_columns))

column_list = ['标准问题', '测试样例', '维度', '标准答案']
result_df = pd.DataFrame(columns=column_list)
first_column_value = df[original_columns[0]]

# print(first_column_value)
for k in range(len(column_list)):
    result_df[column_list[k]] = [np.nan for _ in range(100000)]

# print(result_df)

# for index in range(len(first_column_value)):
#     # print(first_column_value[index])
#     if first_column_value[index] is not np.nan:
#         result_df[column_list[0]][i] = first_column_value[index]
#         i += 1

test = pd.notnull(df[df.columns[0]])
print()


global_dict = OrderedDict()
for m in range(len(test)):
    if test[m]:
        global_dict[m] = df[df.columns[0]][m]

# print(global_dict)

key_list = []
value_list = []
map_key = global_dict.keys()
map_value = global_dict.values()

for key, value in global_dict.items():
    key_list.append(key)
    value_list.append(value)

# print(dir(global_dict))
# print(dir(map_key))

print(key_list)
print(value_list)

i = 0
for key in range(len(key_list)):
    try:
        left = key_list[key]
        right = key_list[key+1]

        first_value = []
        test_example = []
        weidu_list = []
        standard_answer = []

        for n in range(left, right):
            if df[original_columns[0]][n] is not np.nan:
                first_value.append(df[original_columns[0]][n])
            if df[original_columns[2]][n] is not np.nan:
                test_example.append(df[original_columns[2]][n])
            if df[original_columns[3]][n] is not np.nan:
                weidu_list.append(df[original_columns[3]][n])
            if df[original_columns[4]][n] is not np.nan:
                standard_answer.append(df[original_columns[4]][n])

        max_num = max([len(test_example), len(weidu_list), len(standard_answer)])

        for n in range(max_num):
            try:
                result_df[column_list[0]][i] = first_value[n]
            except:
                result_df[column_list[0]][i] = np.nan
            try:
                result_df[column_list[1]][i] = test_example[n]
            except:
                result_df[column_list[1]][i] = np.nan
            try:
                result_df[column_list[2]][i] = weidu_list[n]
            except:
                result_df[column_list[2]][i] = np.nan
            try:
                # standard_answer[n] = standard_answer[n].replace('\n', '')
                result_df[column_list[3]][i] = standard_answer[n]
            except:
                result_df[column_list[3]][i] = np.nan
            # result_df[column_list[1]][i] = df[original_columns[2]][n]
            # result_df[column_list[2]][i] = df[original_columns[3]][n]
            # result_df[column_list[3]][i] = df[original_columns[4]][n]
            # if df[original_columns[0]][n] is not np.nan:
            #     result_df[column_list[0]][i] = df[original_columns[0]][n]
            i += 1
    except:
        print('error!!!')

result_df.to_csv('test.csv', encoding='gb18030', index=False)
print(time.time() - start)