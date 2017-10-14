#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-14 17:39
# Author  : MrFiona
# File    : joseph_ring.py
# Software: PyCharm Community Edition


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