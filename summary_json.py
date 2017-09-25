#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-09-16 17:40
# Author  : MrFiona
# File    : summary_json.py
# Software: PyCharm Community Edition



# import json
#
#
#
# test = ['b','c','d','b','c','a','a']
# # test.sort()
# print test
# test = list(set(test))
# print test
#
#
# def foo(x):
#     print "executing foo(%s)"%(x)
#
# class A(object):
#     def foo(self,x):
#         print "executing foo(%s,%s)"%(self,x)
#
#     @classmethod
#     def class_foo(cls,x):
#         print "executing class_foo(%s,%s)"%(cls,x)
#
#     @staticmethod
#     def static_foo(x):
#         print "executing static_foo(%s)"%x
#
# a=A()
# a.foo(100)
# a.class_foo(300)
# a.static_foo(400)
#
# A.class_foo('grgr')
# A.static_foo('HH')


import multiprocessing
import time
def func(msg):
  for i in xrange(3):
    print msg
    # time.sleep(2)
  return "done " + msg



if __name__ == "__main__":
  start = time.time()
  pool = multiprocessing.Pool(processes=4)
  result = []
  for i in xrange(10):
    msg = "hello %d" %(i)
    result.append(pool.apply_async(func, (msg, )))
  pool.close()
  pool.join()
  for res in result:
    print res.get()
  print "Sub-process(es) done."
  print time.time() - start


