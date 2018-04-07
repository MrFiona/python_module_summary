#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-04-07 22:44
# Author  : MrFiona
# File    : 单例.py
# Software: PyCharm

from functools import wraps



# 2、使用装饰器
def SingletonByDecorator(cls):
    _instance = {}

    @wraps(cls)
    def _singleton(*arg, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*arg, **kwargs)
        return _instance[cls]

    return _singleton

@SingletonByDecorator
class A:
    a = 1

    def __init__(self, x=0):
        self.x = x

a1 = A(10)
a2 = A(20)

if a1 is a2:
    print('a1 equal to a2')
else:
    print('false')


import threading
# 3、这种方式实现的单例模式，使用时会有限制，以后实例化必须通过 obj = Singleton.instance()
# 线程安全的单例模式
class SingletonByMethod:
    _instance_lock = threading.Lock()

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(SingletonByMethod, '_instance'):
            with SingletonByMethod._instance_lock:
                if not hasattr(SingletonByMethod, '_instance'):
                    SingletonByMethod._instance = SingletonByMethod()
        return SingletonByMethod._instance


#4、 基于__new__方法实现（推荐使用，方便）
# 当我们实现单例时，为了保证线程安全需要在内部加入锁
# 我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__）
# 实例化对象；然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式
# 采用这种方式的单例模式，以后实例化对象时，和平时实例化对象的方法一样 obj = Singleton()
class SingletonByNew(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(SingletonByNew, '_instance'):
            with SingletonByNew._instance_lock:
                if not hasattr(SingletonByNew, '_instance'):
                    SingletonByNew._instance = object.__new__(cls)
        return SingletonByNew._instance




if __name__ == '__main__':
    test2 = SingletonByMethod.instance()
    test3 = SingletonByMethod.instance()

    def task(arg):
        obj = SingletonByMethod.instance()
        print(obj)

    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()

    if test2 is test3:
        print('test2 is equal to test3')
    else:
        print('false')

    test4 = SingletonByNew()
    test5 = SingletonByNew()

    if test4 is test5:
        print('test4 is equal to test5')
    else:
        print('false')

    def func(arg):
        obj = SingletonByNew()
        print(obj)

    for i in range(10):
        t = threading.Thread(target=func, args=(i, ))
        t.start()
