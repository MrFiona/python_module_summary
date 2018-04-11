#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-04-10 23:22
# Author  : MrFiona
# File    : test_server.py
# Software: PyCharm



def test(string_io, num):
    string_io.write('test scripts')
    print('哈哈哈是大坏蛋请问请问')
    new_file(num)


def new_file(num):
    with open('test_%s.txt' % str(num), 'w') as p:
        p.write(str(num))
