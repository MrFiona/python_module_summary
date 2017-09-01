#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-08-31 18:15
# Author  : MrFiona
# File    : decorator_wrap.py
# Software: PyCharm


#todo 装饰器总结

# todo 装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。
# todo 装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
# todo 概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能


from functools import wraps


# todo ********************************** 1、最简单的装饰函数的装饰器 **********************************
def decorator_func(func):
    def wrapper():
        print 'before func() called.'
        func()
        #todo 名称变成了wrapper
        print wrapper.__name__
        print 'after func() called.'
    return wrapper

@decorator_func
def test_func():
    a = 1
    print 'this is func.'

print '\033[31m1、最简单的装饰函数的装饰器\033[0m'
test_func()
print '\033[31m1、最简单的装饰函数的装饰器\033[0m'
# todo ********************************** 1、最简单的装饰函数的装饰器 **********************************



# todo ***************************** 2、保持原有被装饰函数特性不变的装饰器 *****************************
def decorator_func(func):
    @wraps(func)
    def wrapper():
        print 'before func() called.'
        func()
        #todo 名称依然为test_func
        print wrapper.__name__
        print 'after func() called.'
    return wrapper

@decorator_func
def test_func():
    a = 1
    print 'this is func.'

print '\n\033[32m2、保持原有被装饰函数特性不变的装饰器\033[0m'
test_func()
print '\033[32m2、保持原有被装饰函数特性不变的装饰器\033[0m'
# todo ***************************** 2、保持原有被装饰函数特性不变的装饰器 *****************************



# todo ********************************* 3、装饰带有参数的函数的装饰器 *********************************
def decorator_func(func):
    @wraps(func)
    def wrapper(a, b):
        print 'before func() called.'
        func(a, b)
        print 'this is wraps:\ta = {}\tb = {}' .format(a, b)
        print 'after func() called.'
    return wrapper

@decorator_func
def test_func(a, b):
    print 'this is func:\ta = {}\tb = {}' .format(a, b)

print '\n\033[36m3、装饰带有参数的函数的装饰器\033[0m'
test_func(a='hello', b='world')
print '\033[36m3、装饰带有参数的函数的装饰器\033[0m'
# todo ********************************* 3、装饰带有参数的函数的装饰器 *********************************



# todo ****************************** 4、装饰带有不固定参数的函数的装饰器 ******************************
def decorator_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print 'before func() called.'
        # todo 不要写成 func(args, kwargs)这样就变成可两个固定参数
        func(*args, **kwargs)
        print 'this is wraps:\targs = {}\tkwargs = {}' .format(args, kwargs)
        print 'after func() called.'
    return wrapper

@decorator_func
def test_func(*args, **kwargs):
    print 'this is func:\targs = {}\tkwargs = {}' .format(args, kwargs)

print '\n\033[35m4、装饰带有不固定参数的函数的装饰器\033[0m'
test_func(100, 'decorator', a='hello', b='world')
print '\033[35m4、装饰带有不固定参数的函数的装饰器\033[0m'
# todo ****************************** 4、装饰带有不固定参数的函数的装饰器 ******************************



# todo *********************************** 5、装饰器带有参数的装饰器 ***********************************
def out_decorator(arg):
    def decorator_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print 'before func() called.'
            # todo 不要写成 func(args, kwargs)这样就变成可两个固定参数
            func(*args, **kwargs)
            print 'this is wraps 1:\targs = {}\tkwargs = {}\targ = {}' .format(args, kwargs, arg)
            print 'this is wraps 2:\targs = {}\tkwargs = {}\targ = {}' .format(args, kwargs, arg)
            print 'after func() called.'
        return wrapper
    return decorator_func

@out_decorator('test_decorator_parameter')
def test_func(*args, **kwargs):
    print 'this is func:\targs = {}\tkwargs = {}' .format(args, kwargs)

print '\n\033[33m5、装饰器带有参数的装饰器\033[0m'
test_func(100, 'decorator', a='hello', b='world')
print '\033[33m5、装饰器带有参数的装饰器\033[0m'
# todo ************************************** 5、带有参数的装饰器 **************************************



# todo *********************************** 6、带有类方法参数的装饰器 ***********************************
class TestLock:
    #todo staticmethod和classmethod作为静态和类装饰器是类的方法,可以直接通过类而不通过实力进行调用
    def __init__(self):
        print 'TestLock.__init__ is called.'

    @staticmethod
    def  acquire():
        print 'TestLock.acquire is called. This is a static method(这是静态方法, 不需要对象实例).'

    @classmethod
    def release(cls):
        print 'TestLock.release is called. This is a class method(这是类方法, 不需要对象实例).'


def out_decorator(cls):
    def decorator_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print 'before func() called.'
            cls.acquire()
            try:
                # todo 不要写成 func(args, kwargs)这样就变成可两个固定参数
                func(*args, **kwargs)
                print 'this is wraps 1:\targs = {}\tkwargs = {}\targ = {}' .format(args, kwargs, cls)
                print 'this is wraps 2:\targs = {}\tkwargs = {}\targ = {}' .format(args, kwargs, cls)
                print 'after func() called.'
            finally:
                cls.release()
        return wrapper
    return decorator_func

@out_decorator(TestLock)
def test_func(*args, **kwargs):
    print 'this is func:\targs = {}\tkwargs = {}' .format(args, kwargs)

print '\n\033[32m6、装饰器带有参数的装饰器\033[0m'
test_func(100, 'decorator', a='hello', b='world')
print '\033[32m6、装饰器带有参数的装饰器\033[0m'
# todo *********************************** 6、带有类方法参数的装饰器 ***********************************



# todo ********************* 7、带有类方法参数的装饰器并对同一个函数应用多个装饰器 **********************
class mylocker:
    def __init__(self):
        print("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print("mylocker.unlock() called.")


class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("lockerex.unlock() called.")


def out_decorator(cls):
    def decorator_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print 'before func() called.'
            cls.acquire()
            try:
                # todo 不要写成 func(args, kwargs)这样就变成可两个固定参数
                print 'this is wraps 1:\targs = {}\tkwargs = {}\targ = {}'.format(args, kwargs, cls)
                print 'this is wraps 2:\targs = {}\tkwargs = {}\targ = {}'.format(args, kwargs, cls)
                print 'after func() called.'
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return wrapper
    return decorator_func


class example:
    @out_decorator(mylocker)
    def myfunc(self, a, b):
        print(" myfunc() called.")
        return a + b

    @out_decorator(mylocker)
    @out_decorator(lockerex)
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a + b


print '\n\033[31m7、装饰器带有参数的装饰器\033[0m'
a = example()
a.myfunc('200 + ', 'string parameter')
print(a.myfunc('3000 + ', 'hello'))
print(a.myfunc2(1, 2))
print(a.myfunc2(3, 4))
print '\033[31m7、装饰器带有参数的装饰器\033[0m'
# todo ********************* 7、带有类方法参数的装饰器并对同一个函数应用多个装饰器 **********************



# todo ********************************* 8、一个多兼容种情况的装饰器 **********************************
# todo 装饰器当传进参数为字符串和非字符串两种情况分别做处理
def log(obj):
    print type(obj)
    if isinstance(obj,str):
        text=obj
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kw):
                print 'begin1 %s %s():' % (text,func.__name__)
                func(*args, **kw)
                print 'args: ', args
                print 'kwargs: ', kw
                print 'obj:', obj, '\t', type(obj)
                print 'end1 %s %s():' % (text,func.__name__)
            return wrapper
        return decorator
    else:
        func=obj
        print func
        @wraps(func)
        def wrapper(*args, **kw):
            print 'begin2 %s():' % (func.__name__)
            func(*args, **kw)
            print 'args: ', args
            print 'kwargs: ', kw
            print 'obj:', obj, '\t', obj.__name__, '\t', type(obj)
            print 'end2 %s():' % (func.__name__)
        return wrapper


@log
def my_test1(ID,student='MrFiona'):
    print 'my_test1 run'

@log('hello')
def my_test(ID,student='MrFiona'):
    print 'my_test run'


print '\033[36m8、一个多兼容种情况的装饰器\033[0m'
my_test1(ID=1024, student='John')
my_test(ID=1024, student='John')
print '\033[36m8、一个多兼容种情况的装饰器\033[0m'
# todo ********************************* 8、一个多兼容种情况的装饰器 **********************************