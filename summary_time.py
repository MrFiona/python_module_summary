#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-01 05:18
# Author  : MrFiona
# File    : summary_time.py
# Software: PyCharm Community Edition



#epoch 格林威治天文时间

import time

print '\033[35m******************************************************************************************************\033[0m'
print '\033[36mtime的接口如下所示:\033[0m\t'
print
print '\033[31m将当前的时间用自epoch时间起点的秒表示:\ttime.time():\t\033[0m', time.time()
print

print '\033[31mepoch时间起点的元祖表示:\ttime.gmtime(0):\t\033[0m', time.gmtime(0)
print '\033[31m将epoch时间起点的小数秒转化为UTC时间的字符串表示:\ttime.asctime(time.gmtime(0):\t\033[0m', time.asctime(time.gmtime(0))
print

print '\033[34m将当前时间的小数秒转化为当前的UTC时间的字符串表示:\ttime.asctime(time.gmtime(time.time())):\t\033[0m', time.asctime(time.gmtime(time.time()))
print "\033[34m将当前时间的小数秒转化为当前的UTC时间的字符串表示:\ttime.strftime('%Y-%m-%d %H-%M-%S', time.gmtime(time.time())):\t\033[0m", time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime(time.time()))
print

print '\033[34m将当前时间的小数秒转化为当前的epoch时间的字符串表示:\ttime.asctime(time.localtime(time.time())):\t\033[0m', time.asctime(time.localtime(time.time()))
print "\033[34m将当前时间的小数秒转化为当前的epoch时间的字符串表示:\ttime.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time())):\t\033[0m", time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
print

print "\033[31m将epoch时间起点的小数秒转化为UTC时间的字符串表示:\ttime.asctime(time.gmtime(0)):\t\033[0m\t", time.asctime(time.gmtime(0))
print "\033[31m将epoch时间起点的小数秒转化为UTC时间的字符串表示:\ttime.strftime('%Y-%m-%d %H-%M-%S', time.gmtime(0)):\t\033[0m\t", time.strftime('%Y-%m-%d %H-%M-%S', time.gmtime(0))
print

print '\033[32mepoch时间起点的元祖表示:\ttime.localtime(time.time()):\t\033[0m\t', time.localtime(time.time())
print time.mktime(time.localtime(time.time()))
print '\033[35m******************************************************************************************************\033[0m\n'




# epoch_tuple_time = time.gmtime(0)
# print '\033[31m获取时间起点epoch时间元祖 time.gmtime(0):\033[0m\t', epoch_tuple_time
# g = time.gmtime(time.time())
# print '\033[32m获取自epoch时间起点算起的当前的时间 time.gmtime(time.time()):\033[0m\t', g
# local_tuple_time = time.localtime(time.time())
# print epoch_tuple_time
# print time.asctime(epoch_tuple_time)
# print time.asctime(g)
# print time.asctime(local_tuple_time)
