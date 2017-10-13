#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-13 22:59
# Author  : MrFiona
# File    : summary_numpy.py
# Software: PyCharm Community Edition



import numpy as np

#todo reshape行数列数乘积需要保证等于6
array_1 =  np.arange(6)
x = array_1.reshape((2,3))
print x

#todo arange类似于python的range函数
array_2 = np.arange(1, 10, 2, dtype=np.float)
print array_2

print '维度数量：', x.ndim
print '数组的形状：', x.shape
print '数组的元素类型：', x.dtype
print '数组的元素数量：', x.size

array_3 = np.array(range(4, 20, 2), dtype=np.int)
array_4 = np.array([[1,2,324], [23,45,76]])
print array_3
print array_4

array_one = np.ones(3, dtype=np.int)
array_one_1 = np.ones((3,4), dtype=np.int)
print array_one
print array_one_1

array_empty = np.empty(3)
array_empty_1 = np.empty((3,4), dtype=np.int)
#todo 不指定数据类型则默认是float类型,数据则是浮点型随机数据
array_empty_2 = np.empty((3,4))
print array_empty
print array_empty_1
print array_empty_2

array_zeros = np.zeros(3)
array_zeros_1 = np.zeros((3,4), dtype=np.int)
#todo 不指定数据类型则默认是float类型
array_zeros_2 = np.zeros((3,4))
print array_zeros
print array_zeros_1
print array_zeros_2

#todo 改变已有数组的数据类型
print x.dtype
change_x = x.astype(np.float)
print change_x.dtype