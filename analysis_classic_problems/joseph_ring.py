#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-14 17:39
# Author  : MrFiona
# File    : joseph_ring.py
# Software: PyCharm Community Edition


#todo 约瑟夫环问题

"""
        约瑟夫环（约瑟夫问题）是一个数学的应用问题：已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。
        从编号为k的人开始报数，数到m的那个人出列；他的下一个人又从1开始报数，数到m的那个人又出列；
        依此规律重复下去，直到圆桌周围的人全部出列
"""

import time


array_num_list = [num for num in range(1, 101)]
print array_num_list

k = 0
m = 5
temp = 0

start = time.time()

while sum(array_num_list):
    k = temp
    for ele in array_num_list:
        if ele != 0:
            k += 1
            temp += 1
        if k == m:
            # time.sleep(1)
            k = 0
            temp = 0
            array_num_list[array_num_list.index(ele)] = 0
            print '编号为 %d 的人出局:\t', ele
            # print 'array_num_list:\t', array_num_list

print time.time() - start