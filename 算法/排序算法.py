#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-01-15 20:05
# Author  : MrFiona
# File    : 排序算法.py
# Software: PyCharm


import time
import numpy as np


start = time.time()
np.random.seed(100)
init_num = np.random.randint(1,500,100)
print(init_num)
"""
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列
"""
#todo 快速排序
def quick_sort(init_num, left, right):
    if left >= right:
        return init_num
    low = left
    high = right
    key = init_num[left]
    # print(left, init_num[left], init_num)
    while left < right:
        while left < right and init_num[right] >= key:
            right -= 1
        init_num[left] = init_num[right]
        while left < right and init_num[left] <= key:
            left += 1
        init_num[right] = init_num[left]
    init_num[right] = key
    quick_sort(init_num, low, left-1)
    quick_sort(init_num, left+1, high)
    return init_num

# a = quick_sort(init_num, 0, len(init_num)-1)
# print(a)

#todo 归并排序
def merge(left, right):
    index_l, index_r = 0, 0
    result = []
    while index_l < len(left) and index_r < len(right):
        if left[index_l] <= right[index_r]:
            result.append(left[index_l])
            index_l += 1
        else:
            result.append(right[index_r])
            index_r += 1
    result.extend(left[index_l:]) if index_r == len(right) else result.extend(right[index_r:])
    return result

def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    num = len(num_list) // 2
    left = merge_sort(num_list[:num])
    right = merge_sort(num_list[num:])
    return merge(left, right)

# a = merge_sort(init_num)
# print(a, len(a))


#todo 堆排序
"""
堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。
可以利用数组的特点快速定位指定索引的元素。堆分为大根堆和小根堆，是完全二叉树。
大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。
"""
def MAX_Heapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点

    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度当独拿出来方便
    for i in xrange((HeapSize -2)//2,-1,-1):#从后往前出数
        MAX_Heapify(heap,HeapSize,i)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    return heap

HeapSort(init_num)
print(init_num)

"""
插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，
时间复杂度为O(n^2)。是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外
（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中
"""
#todo 插入排序
def insert_sort(num_list):
   length = len(num_list)
   for i in range(1, length):
       key = num_list[i]
       j = i-1
       while j >= 0:
           if num_list[j] > key:
               num_list[j+1] = num_list[j]
               num_list[j] = key
           j -= 1
   return num_list

# a = insert_sort(num_list=init_num)
# print(a)


"""
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成
"""
#todo 冒泡排序
def bubble_sort(num_list):
    length = len(num_list)
    for i in range(0, length):
        for j in range(i+1, length):
            if num_list[i] >= num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list

# a = bubble_sort(init_num)
# print(a)

print time.time() - start