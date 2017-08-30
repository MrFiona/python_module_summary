#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-08-30 22:14
# Author  : MrFiona
# File    : _bisect.py
# Software: PyCharm


import bisect


test_bisect = sorted(['cat', 'dog', 'pig', 'mouse', 'tiger', 'sheep', 'chicken'])
print test_bisect
print bisect.bisect(test_bisect, 'looser')
# print test_bisect
print bisect.bisect_left(test_bisect, 'peqwe')
print test_bisect
