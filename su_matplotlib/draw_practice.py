#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-02 12:03
# Author  : MrFiona
# File    : draw_practice.py
# Software: PyCharm Community Edition


from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from operator import itemgetter

#todo 设置中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('ca_list_copy(2).csv')

print df

#todo zwyx列的平均值
value = df['zwyx'].mean()
#todo 将zwyx列0值取代为该列平均值
df['zwyx'] = df['zwyx'].replace(0,value)

#todo 对zwyx列作平均值统计，其他列作计数统计
for col in df.columns:
    if col == 'zwyx':
        print(col + ' mean:\t', df[col].mean())
    else:
        print(col + ' count:\t', df[col].value_counts())

#todo 得到zwmc字段的唯一值列表
df['zwmc'].unique()

#todo 对dd字段分组
group = df.groupby('dd')

#todo 绘图
city_info_list = []
for ele in group:
    print('max:\t', ele[1]['zwyx'].max())
    city_info_list.append((ele[0], ele[1]['zwyx'].max()))

#todo 保存结果数据
# df.to_excel('result_csv.xls')

def set_label(rects):
    i = 1
    for rect in rects:
        plt.text(i, rect, rect)
        i += 1

#todo 取前10城市
city_info_list.sort(key=itemgetter(1), reverse=True)
top_city_info_list = city_info_list[:10]

fig, ax = plt.subplots()
fig.set_facecolor('peru')
plt.title(u'城市最高薪资对比图', fontsize=15, color='blue')
fig.set_size_inches(w=10, h=6)
x = [ele[0] for ele in top_city_info_list]
y = [str(ele[1]) for ele in top_city_info_list]
ax.plot(range(1, len(y) + 1), y, 'o--r', linewidth=2, mfc='y', mec='b', ms=8, alpha=0.8)
set_label(y)

plt.ylabel(u'最高薪资', fontsize=15, color='m')
plt.xlabel(u'城市', fontsize=15, color='b')


x = [u'城市',u'城市',u'城市']
print dir(ax)

plt.xticks(range(1, 12))
ax.set_xticklabels(x,rotation=-45)
plt.grid(color='peru', linestyle='--')
plt.show()