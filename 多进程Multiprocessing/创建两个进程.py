#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-04 00:05
# Author  : MrFiona
# File    : 例子2.py
# Software: PyCharm Community Edition


import os
import time
from multiprocessing import Process


#两个⼦进程将会调⽤的两个⽅法
def worker_1(interval, parent_id):
    print("worker_1,⽗进程(%d),当前进程(%d)" %(parent_id,os.getpid()))
    t_start = time.time()
    time.sleep(interval) #程序将会被挂起interval秒
    t_end = time.time()
    print("worker_1,执⾏时间为'%0.2f'秒" %(t_end - t_start))


def worker_2(interval, parent_id):
    print("worker_2,⽗进程(%d),当前进程(%d)" %(parent_id,os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("worker_2,执⾏时间为'%0.2f'秒" %(t_end - t_start))



if __name__ == '__main__':
    #输出当前程序的ID
    parent_id = os.getpid()
    print("进程ID：%d" %parent_id)
    #创建两个进程对象，target指向这个进程对象要执⾏的对象名称，
    #args后⾯的元组中，是要传递给worker_1⽅法的参数，
    #因为worker_1⽅法就⼀个interval参数，这⾥传递⼀个整数2给它，
    #如果不指定name参数，默认的进程对象名称为Process-N，N为⼀个递增的整数
    p1=Process(target=worker_1,name='worker_1',args=(2, parent_id))
    p2=Process(target=worker_2,name="worker_2",args=(1, parent_id))
    #使⽤"进程对象名称.start()"来创建并执⾏⼀个⼦进程，
    #这两个进程对象在start后，就会分别去执⾏worker_1和worker_2⽅法中的内容
    p1.start()
    p2.start()
    #同时⽗进程仍然往下执⾏，如果p2进程还在执⾏，将会返回True
    print("p2.is_alive=%s" %p2.is_alive())
    #输出p1和p2进程的别名和pid
    print("p1.name=%s" %p1.name)
    print("p1.pid=%d" %p1.pid)
    print("p2.name=%s" %p2.name)
    print("p2.pid=%d" %p2.pid)
    #join括号中不携带参数，表示⽗进程在这个位置要等待p1进程执⾏完成后，
    #再继续执⾏下⾯的语句，⼀般⽤于进程间的数据同步，如果不写这⼀句，
    #下⾯的is_alive判断将会是True，在shell（cmd）⾥⾯调⽤这个程序时
    #可以完整的看到这个过程，⼤家可以尝试着将下⾯的这条语句改成p1.join(1)，
    #因为p2需要2秒以上才可能执⾏完成，⽗进程等待1秒很可能不能让p1完全执⾏完成，
    #所以下⾯的print会输出True，即p1仍然在执⾏
    p1.join()
    p2.join()
    print("p1.is_alive=%s" %p1.is_alive())