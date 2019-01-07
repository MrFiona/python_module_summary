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
    create_process(multiprocessing.cpu_count(), jobs)
    add_jobs(jobs)
    print(jobs.qsize())
    print(dir(jobs))
    print('results:\t', results.qsize())
    print('dir:\t', dir(results))
    try:
        jobs.join()
    except KeyboardInterrupt:
        print('KeyboardInterrupt: canceling')

def create_process(concurrency, jobs):
    for _ in range(concurrency):
        process = multiprocessing.Process(target=worker, args=(jobs,))
        process.daemon = True
        process.start()

def worker(jobs):
    while True:
        # try:
        if jobs.empty():
            break
        index, df = jobs.get()
        print('index: {}', index)
        scale_one(index, df)
        # finally:
        #     jobs.task_done()
            # print('d:\t', results.qsize())

def scale_one(index, df):
    columns_list = list(df.columns)
    _df = pd.DataFrame(columns=columns_list)
    print(columns_list)
    num_index = 0
    for index in range(len(df)):
        # print(df_set[1].loc[num_index, columns_list])
        # print(num_index)
        _df.loc[num_index, columns_list] = df.loc[df.index[index], columns_list]
        num_index += 1

    _df.to_csv('{}_result.csv'.format(index), index=False, encoding='gb18030')

def add_jobs(jobs):
    read_df = pd.read_csv('zhangpeng_result.csv', encoding='gb18030', chunksize=5000, low_memory=False)
    index = 0
    for df in read_df:
        jobs.put((index, df))
        index += 1
    # for value in range(20):
    #     jobs.put(value)



if  __name__ == '__main__':
    start = time.time()
    scale()
    print(time.time() - start)