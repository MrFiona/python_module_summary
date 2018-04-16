#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-04-16 23:24
# Author  : MrFiona
# File    : test_pandas.py
# Software: PyCharm




import pandas as pd



df = pd.read_excel('zhangpeng_head.xlsx', encoding='gb18030')
result_df = pd.DataFrame(columns=df.columns)
print(dir(df))

# result_df.loc[3, df.columns[2:5]] = df.loc[3, df.columns[2:5]]
# result_df.iloc[0][df.columns[:5]] = df.iloc[0][df.columns[:5]]
# result_df.iloc[df.columns[:5]][1] = df.iloc[df.columns[:5]][1]
# print(df.iloc[0][ df.columns[:5]])
# print(df.iloc[1][ df.columns[:5]])
# print(df.iloc[2][ df.columns[:5]])



# https://blog.csdn.net/pipisorry/article/details/18012125
# SettingWithCopyWarning提示
# SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
# df[len(df.columns) - 1][df[len(df.columns) - 1] > 0.0] = 1.0
# 这个warning主要是第二个索引导致的，就是说第二个索引是copy的。
# 奇怪的是，df的确已经修改了，而warnning提示好像是说修改被修改到df的一个copy上了。所以这里只是一个warnning，只是说和内存有关，可能赋值不上，也可能上了。

# 解决
# 修改df原本数据时建议使用loc，但是要注意行列的索引位置Try using .loc[row_indexer,col_indexer] = value instead
# df.loc[df[len(df.columns) - 1] > 0.0, len(df.columns) - 1] = 1.0