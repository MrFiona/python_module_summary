#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-03 23:52
# Author  : MrFiona
# File    : 例子1.py
# Software: PyCharm Community Edition


import os
from multiprocessing import Process


def run_pro(name):
    print('子进程运行中: name = %s, pid = %d....' %(name, os.getpid()))



if __name__ == '__main__':
    print('父进程 %d.' % os.getpid())
    p = Process(target=run_pro, args=('test multiprocessing',))
    print('子进程将要执行')
    print('子进程是否还在运行?? {}' .format(p.is_alive()))
    p.start()
    print('子进程是否还在运行?? {}' .format(p.is_alive()))
    p.join()
    print('子进程是否还在运行?? {}' .format(p.is_alive()))
    print('子进程结束')