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