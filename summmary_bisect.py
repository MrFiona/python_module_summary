#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-08-30 22:14
# Author  : MrFiona
# File    :summary _bisect.py
# Software: PyCharm


import bisect


test_bisect = sorted(['cat', 'dog', 'pig', 'mouse', 'tiger', 'sheep', 'chicken'])
print test_bisect
print 'default bisect:', bisect.bisect(test_bisect, 'default bisect')
print 'right bisect:', bisect.bisect_right(test_bisect, 'right bisect')
print 'left bisect:', bisect.bisect_left(test_bisect, 'left bisect')
bisect.insort(test_bisect, 'right')
print test_bisect
bisect.insort_right(test_bisect, 'insort right')
print test_bisect
bisect.insort_left(test_bisect, 'insort left')
print test_bisect
