#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-01-15 20:05
# Author  : MrFiona
# File    : 排序算法.py
# Software: PyCharm


import time
import numpy as np

start = time.time()
np.random.seed(10)
random_num = np.random.randint(1, 1000, 2000)
# print random_num, len(random_num)

#todo 插入排序
def insert_sort(random_num):
    for index in xrange(1, len(random_num)):
        key = random_num[index]
        j = index - 1
        while j >= 0:
            if random_num[j] > key:
                random_num[j+1] = random_num[j]
                random_num[j] = key
            j -= 1
    print random_num
    return random_num

#todo 希尔排序
def hill_sort(random_num):
    pass

#todo 冒泡排序
def bubble_sort(random_num):
    for i in xrange(len(random_num)):
        for j in xrange(i+1, len(random_num)):
            if random_num[i] > random_num[j]:
                random_num[i], random_num[j] = random_num[j], random_num[i]
    print random_num
    return random_num

#todo 快速排序
def quick_sort(random_num, left, right):
    if left >= right:
        return random_num

    low = left
    high = right
    key = random_num[left]

    while low < high:
        #todo 右边的大于key则左移一位，当前值位置不变
        while low < high and random_num[high] >= key:
            high -= 1
        #todo 右边的小于左边的则需要将当前值更新为left位置值
        random_num[low] = random_num[high]
        #todo 左边的小于key则右移一位
        while low < high and random_num[low] <= key:
            low += 1
        #todo 左边的大于key则将当前位置值更新为右边位置为high的值
        random_num[high] = random_num[low]

    random_num[low] = key

    quick_sort(random_num, left, low - 1)
    quick_sort(random_num, low + 1, right)
    # print random_num
    return random_num


# print 'insert_sort:\t', time.time() - start
# insert_sort(random_num)
# start = time.time()
# bubble_sort(random_num)
# print 'bubble_sort:\t', time.time() - start
# start = time.time()
print quick_sort(random_num, 0, len(random_num)-1)

print time.time() - start