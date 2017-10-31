#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-31 22:07
# Author  : MrFiona
# File    : numpy_slice.py
# Software: PyCharm Community Edition


import numpy as np

# array = np.random.randint(1, 100, 10)
array = np.random.random((3,4,5))
print array, type(array)

print '1:\t', array[1:, 1:4], type(array[1:, 1:4])
print '11:\t', array[1, 1:4], type(array[1, 1:4])
print '2:\t', array[1, 1:4][1, 1:4]
print '3:\t', array[1, 1:4, 1:3]
print '33:\t', array[1, 1:4, 1:3][1:,1:]
print '4:\t', array[1, 1:4][1:3]
print '5:\t', array[1:, 1:4][1:3]