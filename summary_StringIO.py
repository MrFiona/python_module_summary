#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-04-07 21:52
# Author  : MrFiona
# File    : summary_StringIO.py
# Software: PyCharm

try:
    from _io import StringIO
except ImportError:
    from io import StringIO

f = StringIO()
f.write('hello world!!!')
print(f.getvalue(), len(f.getvalue()))
f.write('hello world!!!')
print(f.getvalue(), len(f.getvalue()))
f.truncate(0)
f.write('start write!')
print(f.tell())
print("next:\t", f.getvalue(), len(f.getvalue()))

f_test = StringIO('Hello! Hi! Goodbye!')
print("1:\t", f_test.read())
print(f_test.getvalue())
print(f_test.getvalue())
print("2:\t", f_test.read())
print("3:\t", f_test.read())
print("4:\t", f_test.read())
print("next:\t", f_test.getvalue(), len(f_test.getvalue()))

f_test.close()
f.close()










