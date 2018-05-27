#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-05-28 01:25
# Author  : MrFiona
# File    : summary_collections.py.py
# Software: PyCharm


import collections
import json


#todo 用defaultdict来构造一颗树形结构
def tree():
    """
    Factory that creates a default dict that also use this factory
    :return:
    """
    return collections.defaultdict(tree)

root = tree()
root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None
print(json.dumps(root, indent=4, sort_keys=True, separators=(',', ':')))

a = collections.Counter('abcdeabcdabcaba')
"""
        >>> c = Counter()                           # a new, empty counter
        >>> c = Counter('gallahad')                 # a new counter from an iterable
        >>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
        >>> c = Counter(a=4, b=2)                   # a new counter from keyword args
"""

print(a)
print(a.most_common(3))
print(sorted(a))
print(sorted(a.elements()))
print(''.join(sorted(a.elements())))
print(sum(a.values()))
print(a['a'])
del a['b']
print(a['b'])
print(a)

d = collections.Counter('simsalabim')
a.update(d)
print(a['a'])
a.clear()
print(a)

c = collections.Counter('aaabbc')
c['b'] -= 2
print(c.most_common())