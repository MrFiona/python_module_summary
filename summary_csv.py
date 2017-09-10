#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-09-10 21:19
# Author  : MrFiona
# File    : summary_csv.py
# Software: PyCharm Community Edition



import csv

insert_value_list = []

with open('test_csv.csv', 'rb') as f:
    reader1 = csv.reader(f)

    for row in reader1:
        print row
        insert_value_list.append(row)


with open('test_csv4.csv','wb') as f:
    csv_writer = csv.writer(f)
    for row in insert_value_list:
        print row
        csv_writer.writerow(row)