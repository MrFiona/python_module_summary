#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-09-03 21:22
# Author  : MrFiona
# File    : file_data_filter.py
# Software: PyCharm


import sys
import os
import argparse


def get_lines(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return lines


def filter(lines, delete_sp, isBlankCut):
    new_lines = []
    for line in lines:
        if isBlankCut and len(line.strip()) == 0:
            continue
        if not line.strip().startswith(delete_sp):
            new_lines.append(line)
    return new_lines


def output(out_path, new_lines):
    with open(out_path, "w") as f:
        f.writelines(new_lines)


# 打印帮助信息
def help_msg():
    print '\033[31m******************** description  *******************************\033[0m'
    print("功能：数据过滤，清理注释行[空行]")
    print("选项:")
    print("\t -f inputfilepath  [必输，原文件路径]")
    print("\t -o outputfilepath [必输，默认为 inputfilepath.dist ]")
    print("\t -F 'FS'           [可选，要去除注释行开始标志，默认为# ]")
    print("\t -b                [可选，是否删除空行,默认不剔除空行 ]")
    print '例如: python file_data_filter.py -f input_file -F -b'
    print '输出文件已经默认指定[ 原文件名+.dist ]'
    print '-F 和 -b可选'
    print '\033[31m******************** description  *******************************\033[0m'
    sys.exit(0)


# 程序入口，读入参数，执行
def main():
    delete_sp = "#"
    isBlankCut = False

    strUsage = "Usage: %prog [option] args"
    parser = argparse.ArgumentParser(usage=strUsage, epilog="And that's how you'd to do", version='1.0', description='A script that used to delete lines that begin with the specified string')
    parser.add_argument('-f', '--infile', action='store', dest='input_file', type=str, help='输入文件路径,必须输入')
    parser.add_argument('-o', '--outfile', dest='output_file', default=os.path.split(__file__)[1] + '.dist', type=str, help='输出文件路径,非必须输入，默认是：原文件+.dist')
    parser.add_argument('-F', '--FS', action='store_true', dest='delete_annotation_flag', help='是否去除注释行开始标记, 非必须输入, 默认注释标记：#')
    parser.add_argument('-d', '--delete_blank', action='store_true', dest='delete_blank_flag', help='是否删除空行标记，非必须输入，默认是：False不删除')
    parser.add_argument('--foo', help='是否删除空行标记，非必须输入，默认是：False不删除')

    # opts= parser.parse_args('-f ../decorator_wrap.py'.split())
    try:
        opts= parser.parse_args()
        print '\033[33m******************** 相关参数  *******************************\033[0m'
        print 'opts:\t', opts
        print 'opts.input_file:\t', opts.input_file
        print 'opts.output_file:\t', opts.output_file
        print 'opts.delete_annotation_flag:\t', opts.delete_annotation_flag
        print 'opts.delete_blank_flag:\t', opts.delete_blank_flag
        print '\033[33m******************** 相关参数  *******************************\033[0m\n'

        if not opts.input_file:
            raise ValueError('请输入待处理文件')

        if not os.path.exists(opts.input_file):
          print(opts.input_file+" file : 输入文件 [ %s ]is not exists" % opts.input_file)
          sys.exit(1)

        lines = get_lines(opts.input_file)
        new_lines = filter(lines, delete_sp, isBlankCut)
        output(opts.output_file, new_lines)
    except (ValueError, TypeError) as e:
        help_msg()
        raise UserWarning('请填写正确的参数格式!')

if __name__ == "__main__":
    import time
    start = time.time()
    main()
    print time.time() - start
