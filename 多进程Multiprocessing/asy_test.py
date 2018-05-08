#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-05-08 22:10
# Author  : MrFiona
# File    : asy_test.py
# Software: PyCharm


import os
import time
import multiprocessing
import pandas as pd


def scale():
    jobs = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    create_process(multiprocessing.cpu_count(), jobs, results)
    add_jobs(jobs)
    print(jobs.qsize())
    print(dir(jobs))
    print('results:\t', results.qsize())
    print('dir:\t', dir(results))
    try:
        jobs.join()
    except KeyboardInterrupt:
        print('KeyboardInterrupt: canceling')

def create_process(concurrency, jobs, results):
    for _ in range(concurrency):
        process = multiprocessing.Process(target=worker, args=(jobs, results))
        process.daemon = True
        process.start()

def worker(jobs, results):
    while True:
        try:
            name = jobs.get()
            result = scale_one(name)
            results.put(result)
        finally:
            jobs.task_done()
            # print('d:\t', results.qsize())

def scale_one(name):
    # time.sleep(1)
    # print('hello world!!!')
    return name

def add_jobs(jobs):
    for value in range(20):
        jobs.put(value)



if  __name__ == '__main__':
    start = time.time()
    scale()
    print(time.time() - start)