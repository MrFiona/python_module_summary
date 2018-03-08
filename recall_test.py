#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-03-08 20:48
# Author  : MrFiona
# File    : recall_test.py
# Software: PyCharm


import re
import sys
import time


def func(a):
    result_com = ''
    with open('Bakerville_100_2017WW32_33_BKC_2017_08_07_15_53_14_log.txt') as p:
        data = p.readlines()
        regex = re.compile(r'\d{4}\\nWW\d{2}')
        for ele in data:
            obj = re.findall(regex, ele)
            if obj:
                result_com = ','.join(obj)
    sys.stdout.write(result_com+''.join(a)+str(len(a)))

func(sys.argv)


# http://blog.csdn.net/cnweike/article/details/73620250

# import sys
# import time
#
# for i in range(5):
#     sys.stdout.write('Processing {}\n'.format(i))
#     sys.stdout.flush()
#     time.sleep(1)
#
# for i in range(5):
#     sys.stderr.write('Error {}\n'.format(i))
#     sys.stderr.flush()
#     time.sleep(1)