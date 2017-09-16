#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-09-16 11:45
# Author  : MrFiona
# File    : summary_pickle.py
# Software: PyCharm Community Edition


try:
    import cPickle as pickle
except ImportError:
    import pickle as pickle


with open('summary_bisect.py', 'rb') as f:
    data = f.readlines()

with open('test.txt', 'wb') as f:
    pickle.dump(data, f)

with open('test.txt', 'rb') as f:
    data = pickle.load(f)

print data


#todo pickle.dumps将python对象序列化 pickle.loads反序列化
with open('test.txt1', 'wb') as f:
    f.write(pickle.dumps(data))

with open('test.txt1', 'rb') as f:
    lines = f.readlines()
    data = pickle.loads(''.join(lines))

print data

