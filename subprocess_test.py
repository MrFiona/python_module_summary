#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-03-08 20:47
# Author  : MrFiona
# File    : subprocess_test.py
# Software: PyCharm


# import shlex
# import subprocess
#
# if __name__ == '__main__':
#     shell_cmd = 'python recall_test.py'
#     f = open('test.txt', 'w')
#     cmd = shlex.split(shell_cmd)
#     p = subprocess.Popen(shell_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     while p.poll() is None:
#         line = p.communicate()[0]
#         # line = p.stdout.readline()
#         # line = line.strip()
#         if line:
#             print('Subprogram output: [{}]'.format(line))
#     if p.returncode == 0:
#         print('Subprogram success')
#     else:
#         print('Subprogram failed')
#     f.close()


import os
import cx_Oracle

import cx_Oracle
conn = cx_Oracle.connect('system/Mrfiona123@127.0.0.1:1521/orcl')
cursor = conn.cursor()
# cursor.execute('select * from tbl_pay_order_info')
# result = cursor.fetchall()
print (cursor.rowcount)
# for row in result:
#     print row#此处特别注意前面空格
cursor.close()
conn.close()

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  #或者
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'

# C:\Program Files\Anaconda3\Library\bin
# C:\Program Files\Anaconda3\Scripts
# C:\Program Files\Anaconda3
# import shlex
# import subprocess
#
# if __name__ == '__main__':
#     shell_cmd = 'python3 subprogram.py'
#     cmd = shlex.split(shell_cmd)
#     p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     while p.poll() is None:
#         line = p.stdout.readline()
#         line = line.strip()
#         if line:
#             print('Subprogram output: [{}]'.format(line))
#     if p.returncode == 0:
#         print('Subprogram success')
#     else:
#         print('Subprogram failed')