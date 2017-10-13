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
print '\033[36mx:\033[0m', x

#todo arange类似于python的range函数
array_2 = np.arange(1, 10, 2, dtype=np.float)
print '\033[36marray_2:\033[0m', array_2

print '\033[32m维度数量：\033[0m', x.ndim
print '\033[32m数组的形状：\033[0m', x.shape
print '\033[32m数组的元素类型：\033[0m', x.dtype
print '\033[32m数组的元素数量：\033[0m', x.size

array_3 = np.array(range(4, 20, 2), dtype=np.int)
array_4 = np.array([[1,2,324], [23,45,76]])
print '\033[32marray_3:\033[0m', array_3
print '\033[32marray_4:\033[0m', array_4

array_one = np.ones(3, dtype=np.int)
array_one_1 = np.ones((3,4), dtype=np.int)
print '\033[32marray_one:\033[0m', array_one
print '\033[32marray_one_1:\033[0m', array_one_1

array_empty = np.empty(3)
array_empty_1 = np.empty((3,4), dtype=np.int)
#todo 不指定数据类型则默认是float类型,数据则是浮点型随机数据
array_empty_2 = np.empty((3,4))
print '\033[35marray_empty:\033[0m', array_empty
print '\033[35marray_empty_1:\033[0m', array_empty_1
print '\033[35marray_empty_2:\033[0m', array_empty_2

array_zeros = np.zeros(3)
array_zeros_1 = np.zeros((3,4), dtype=np.int)
#todo 不指定数据类型则默认是float类型
array_zeros_2 = np.zeros((3,4))
print '\033[35marray_zeros:\033[0m', array_zeros
print '\033[35marray_zeros_1:\033[0m', array_zeros_1
print '\033[35marray_zeros_2:\033[0m', array_zeros_2

#todo 改变已有数组的数据类型
print '\033[32mx.dtype:\033[0m', x.dtype
change_x = x.astype(np.float)
print '\033[32mchange_x.dtype:\033[0m', change_x.dtype

#todo reshape修改数组形状，-1代表当前维度的元素个数，自动计算
reshape_array_3 = array_3.reshape(4,-1)
print '\033[32mreshape_array_3:\033[0m', reshape_array_3

b = np.array([[0, 1], [2, 3]])
m = np.array([[0, 1], [2, 3]])
b.resize((2,1))
m.resize((2,3))
print '\033[36mb:\033[0m', b
print '\033[36mm:\033[0m', m

#todo 矩阵的乘积 其中一个矩阵的行等于另一个矩阵的列
m = np.arange(1, 12, 2)
m = m.reshape((2,3))
print '\033[36mm:\033[0m', m

n = np.arange(2, 14, 2, dtype=np.float)
n = n.reshape((3,2))
print '\033[36mn:\033[0m', n
print '\033[36mnp.dot(m, n):\033[0m', np.dot(m, n)

#todo ndarray-多维数组的索引
test_array = np.array([[[2, 3, 4, 5],
                        [1, 3, 4, 9]],
                       [[0, 3, 4, 8],
                        [2, 4, 9, 4]],
                       [[1, 4, 5, 8],
                        [2, 5, 6, 8]],
                       [[2, 3, 6, 8],
                        [3, 4, 8, 9]]])
print '\033[32mtest_array[1]:\033[0m', test_array[1]
print '\033[32mtest_array[1][0]:\033[0m', test_array[1][0]
print '\033[32mtest_array[1][0][1:3]:\033[0m', test_array[1][0][1:3]
print '\033[32mtest_array[1, :, 1:3]:\033[0m', test_array[1, :, 1:3]
print '\033[32mtest_array[1, :][1:]:\033[0m', test_array[1, :][1:]
print '\033[32mtest_array[1, :][0]:\033[0m', test_array[1, :][0]
print '\033[32mtest_array[1, :]:\033[0m', test_array[1, :]
print '\033[32mtest_array[1][:]:\033[0m', test_array[1][:]

#todo ndarray-布尔类型索引
#todo numpy中不能使用过python的and、or、not操作，使用逻辑与(&)，逻辑或(|)，逻辑非(~)来替换
names = np.array(['Jeff', 'Tom', 'John', 'Lily'])
scores = np.array([[94, 78, 91, 67],
                   [89, 70, 98, 100],
                   [80, 79, 82, 92],
                   [100, 59, 93, 95]])
classes = np.array([u'语文', u'英语', u'物理', u'数学'])
print "\033[35mscores[names == 'Jeff']:\t\033[0m", scores[names == 'Jeff']
print "\033[35mscores[names == 'Jeff'].reshape((-1,))[classes == u'物理']:\t\033[0m", scores[names == 'Jeff'].reshape((-1,))[classes == u'物理']
print "\033[35mscores[(names == 'Jeff') | (names == 'Lily')]:\t\033[0m", scores[(names == 'Jeff') | (names == 'Lily')]
print "\033[35mscores[(names != 'Jeff') & (names != 'Lily') & (names != 'John')]:\t\033[0m", scores[(names != 'Jeff') & (names != 'Lily') & (names != 'John')]

#todo ndarray-花式索引
array = np.arange(32).reshape(8, 4)
print 'array:\t', array, type(array)
#todo 获取第0、3、5行的数据
print '获取第0、3、5行的数据:\n', array[[0, 3, 5]]
#todo 获取第(0, 0)，(3, 3)，(5, 3)这三个索引位置的数据
print '获取第(0, 0)，(3, 3)，(5, 3)这三个索引位置的数据:', array[[0,3,5],[0,3,3]]
#todo 获取第0、3、5行的第0、2、3列的数据
print '获取第0、3、5行的第0、2、3列的数据:', array[[0,3,5]].T[[0,2,3]].T #通过转置矩阵实现
print '获取第0、3、5行的第0、2、3列的数据:', array[np.ix_([0,3,5],[0,2,3])]
#todo np.ix_函数会产生一个索引器
print 'np.ix_函数会产生一个索引器:', np.ix_([0,3,5],[0,2,3])

#todo 数组的转置是指将shape进行重置操作，并将其值重置为原始shape元祖的倒置，比如原始的shape值为：(2,3,4),转置后的新元祖shape值为（4,3,2）
#todo 对于二维数组而言(矩阵)数组的转置其实就是矩阵的的转置
#todo 可以通过调用数组的transpose函数或者T属性进行数组转置操作