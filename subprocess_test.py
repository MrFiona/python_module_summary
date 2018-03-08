#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-03-08 20:47
# Author  : MrFiona
# File    : subprocess_test.py
# Software: PyCharm


import shlex
import subprocess

if __name__ == '__main__':
    shell_cmd = 'python recall_test.py'
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(shell_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.communicate()[0]
        # line = p.stdout.readline()
        line = line.strip()
        if line:
            print('Subprogram output: [{}]'.format(line))
    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')





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