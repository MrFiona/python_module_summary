#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-11-04 00:50
# Author  : MrFiona
# File    : 进程池创建进程.py
# Software: PyCharm Community Edition


from multiprocessing import Pool, process
import os,time,random


def worker(msg):
    t_start = time.time()
    print("%s开始执⾏,进程号为%d" %(msg, os.getpid()))
    #random.random()随机⽣成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print("%s 执⾏完毕，耗时%0.2f" %(msg, t_stop-t_start))


if __name__ == '__main__':
    po=Pool(3) #定义⼀个进程池，最⼤进程数3
    for i in range(0,10):
        # Pool.apply_async(要调⽤的⽬标,(传递给⽬标的参数元祖,))
        # 每次循环将会⽤空闲出来的⼦进程去调⽤⽬标
        po.apply_async(worker,(i,))
        # po.apply(worker,(i,))
    print("----start----")
    po.close() #关闭进程池，关闭后po不再接收新的请求
    po.join() #等待po中所有⼦进程执⾏完成，必须放在close语句之后
    print("-----end-----")


    """
        multiprocessing.Pool常⽤函数解析：
            1、apply_async(func[, args[, kwds]]) ：使⽤⾮阻塞⽅式调⽤func（并⾏执
            ⾏，堵塞⽅式必须等待上⼀个进程退出才能执⾏下⼀个进程），args为
            传递给func的参数列表，kwds为传递给func的关键字参数列表；
            2、apply(func[, args[, kwds]])：使⽤阻塞⽅式调⽤func
            3、close()：关闭Pool，使其不再接受新的任务；
            4、terminate()：不管任务是否完成，⽴即终⽌；
            5、join()：主进程阻塞，等待⼦进程的退出， 必须在close或terminate之后使⽤；
    """