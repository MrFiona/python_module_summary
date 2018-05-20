#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-05-20 02:40
# Author  : MrFiona
# File    : map_multi_threading.py
# Software: PyCharm


import time
import tqdm
import numpy as np
import pandas as pd
from multiprocessing import Pool, Process


def create_csv(df_set):
    columns_list = list(df_set[1].columns)
    df = pd.DataFrame(columns=columns_list)
    print(columns_list)
    num_index = 0
    for index in range(len(df_set[1])):
        # print(df_set[1].loc[num_index, columns_list])
        print(num_index)
        df.loc[num_index, columns_list] = df_set[1].loc[df_set[1].index[index], columns_list]
        num_index += 1

    df.to_csv('{}_result.csv'.format(df_set[0]), index=False, encoding='gb18030')


if __name__ == '__main__':
    start = time.time()
    index = 0

    # #todo 1 57s
    # read_df = pd.read_csv('zhangpeng_result.csv', encoding='gb18030', low_memory=False)
    # step = 10
    # index_range_list = [(i, read_df.loc[i*len(read_df)//step:(i+1)*len(read_df)//step]) for i in range(0, step)]
    # pool = Pool()
    # # pool.map(create_csv, result_df)
    # for df in index_range_list:
    #     pool.apply_async(create_csv, args=(df,))
    # pool.close()
    # pool.join()
    # #todo 1 57s

    # #todo 2 59s左右
    # read_df = pd.read_csv('zhangpeng_result.csv', encoding='gb18030', low_memory=False)
    # step = 10
    # index_range_list = [(i, read_df.loc[i * len(read_df) // step:(i + 1) * len(read_df) // step]) for i in range(0, step)]
    # jobs = [Process(target=create_csv, args=(original_df,)) for original_df in index_range_list]
    # print(jobs)
    # for job in jobs:
    #     job.start()
    # for job in jobs:
    #     job.join()
    # #todo 2 59s左右

    # #todo 3 144左右
    # read_df = pd.read_csv('zhangpeng_result.csv', encoding='gb18030', low_memory=False)
    # step = 10
    # index_range_list = [(i, read_df.loc[i * len(read_df) // step:(i + 1) * len(read_df) // step]) for i in range(0, step)]
    # for df in index_range_list:
    #     columns_list = list(df[1].columns)
    #     df_ = pd.DataFrame(columns=columns_list)
    #     num_index = 0
    #     for i in range(len(df[1])):
    #         df_.loc[num_index, columns_list] = df[1].loc[df[1].index[i], columns_list]
    #         num_index += 1
    #         print(num_index)
    #     df_.to_csv('{}_{}_result.csv'.format(index, index), index=False, encoding='gb18030')
    #     index += 1
    # #todo 3 144左右
    print(time.time() - start)

