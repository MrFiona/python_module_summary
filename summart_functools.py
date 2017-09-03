#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-09-03 10:16
# Author  : MrFiona
# File    : summart_functools.py
# Software: PyCharm


"""
    functools 模块提供了高阶函数功能：函数可以作为或者返回其他函数。通常，为了本模块的目的，任何可调用对象都可以被视为功能
"""


import _functools
import functools


#todo functools.partial(func[,*args][, **keywords]) 返回一个新的 partial 对象，该对象被调用的时候，其行为像调用带位置参数 args 和关键字参数 keywords 的函数 func 。
#todo 如果提供多个参数调用， 它们会被追加给 args。如果提供额外的关键字参数， 它们会扩展和覆盖 keywords

#todo 实现版本
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords

#todo partial() 用于偏函数应用。偏函数是指把一个函数的部分位置参数和/或关键字参数“冻结”，返回一个新的简化了的函数对象。
#todo 典型的，函数在执行时，要带上所有必要的参数进行调用。然后，有时参数可以在函数被调用之前提前获知。
#todo 这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用

#todo 举例
def add_func(a, b):
    return a + b

print add_func(3, 4)
plus_2 = functools.partial(add_func, b=2)
plus_2_func = functools.partial(add_func, b=2).func
plus_2_args = functools.partial(add_func, b=2).args
plus_2_keywords = functools.partial(add_func, b=2).keywords
plus_2_dict = functools.partial(add_func, b=2).__dict__
plus_2_doc = functools.partial(add_func, b=2).__doc__
print 'func:\t', plus_2_func
print 'args:\t', plus_2_args
print 'keywords:\t', plus_2_keywords
print '__dict__:\t', plus_2_dict
print '__doc__:\t', plus_2_doc
plus_5 = functools.partial(add_func, b=5)
print plus_2(10)
print plus_5(10)



#todo functools.update_wrapper(wrapper, wrapped[, assigned][, updated]) 更新一个 wrapper 函数让其更像一个 wrapped 函数。可选的参数是一个元祖，
#todo 来指定原函数哪些属性被直接分配给装饰器中的匹配属性 ，哪些装饰器属性使用来自原函数的相应属性来更新。
#todo 这些参数的默认值是模块级别的常数 WRAPPER_ASSIGNMENTS (分配给包装器函数： __name__, __module__ 和 __doc__, 文档字符串) 和 WRAPPER_UPDATES (更新包装器函数： __dict__, 等实例的字典).

def wrap(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it"""
        print 'before call'
        return func(*args, **kwargs)
    return call_it

@wrap
def hello():
    """say hello"""
    print 'hello world'

from functools import update_wrapper
def wrap2(func):
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print 'before call'
        return func(*args, **kwargs)
    return update_wrapper(call_it, func)

@wrap2
def hello2():
    """test hello"""
    print 'hello world2'


#todo 这个函数主要用在装饰器函数中，装饰器返回函数反射得到的是包装函数的函数定义而不是原始函数定义

hello()
print hello.__name__
print hello.__doc__

print
hello2()
print hello2.__name__
print hello2.__doc__



#todo functools.wraps(wrapped[, assigned][, updated]) 这是用来调用 functools.partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)
#todo 函数的方便函数。当定义一个包装函数的时候作为一个函数装饰器

def wrap3(func):
    @functools.wraps(func)
    def call_it(*args, **kwargs):
        """wrap func: call_it2"""
        print 'before call'
        return func(*args, **kwargs)
    return call_it

@wrap3
def hello3():
    """test hello 3"""
    print 'hello world3'

print
hello3()



#todo functools.reduce(function, iterable[, initializer]) 等同于内置函数reduce() 用这个的原因是使代码更兼容(python3)
print functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 10)



#todo functools.cmp_to_key(func) 把一个老式的比较函数转换为一个关键函数。需要和接受关键函数作为参数的函数一起使用 (比如 sorted(), min(), max(),
# todo heapq.nlargest(), heapq.nsmallest(), itertools.groupby()).当程序转换到 Python 3 后比较函数不再被支持， 这个函数主要用来实现这种转换的工具。
# todo 比较函数是任何一个可调用的函数，且包含两个参数，对参数进行比较，如果小于返回负数，等于返回0，大于返回正数。关键函数是一种可调用函数。
# todo 接受一个参数，返回另一个表明其在期望序列中的位置的值

#todo key函数，接收一个参数，返回一个表明该参数在期望序列中的位置 例如: sorted(iterable, key=cmp_to_key(locale.strcoll))  # locale-aware sort order
key_asc = functools.cmp_to_key(lambda x,y: int(x) - int(y))
key_desc = functools.cmp_to_key(lambda x,y: int(y) - int(x))
print sorted(['432','65','456547'], key=key_asc)
print sorted(['432','65','456547'], key=key_desc)



#todo functools.total_ordering(cls) 给定一个定义了一个或多个富比较排序方法的类，该方法提供了一个类装饰器。这简化了指定所有可能的富比较操作的工作量。
#todo 这个类必须要定义 __lt__(), __le__(), __gt__(), 或 __ge__()方法中的任何一个。此外， 这个类还应该提供一个 __eq__() 方法但不是必须。 示例：

@functools.total_ordering
class Student:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    def __eq__(self, other):
        print ((self.lastname.lower(), self.firstname.lower()),
                (other.lastname.lower(), other.firstname.lower())),
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        print ((self.lastname.lower(), self.firstname.lower()),
                (other.lastname.lower(), other.firstname.lower())),
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
    def __le__(self, other):
        print ((self.lastname.lower(), self.firstname.lower()),
                (other.lastname.lower(), other.firstname.lower())),
        return ((self.lastname.lower(), self.firstname.lower()) <=
                (other.lastname.lower(), other.firstname.lower()))
    def __gt__(self, other):
        print ((self.lastname.lower(), self.firstname.lower()),
                (other.lastname.lower(), other.firstname.lower())),
        return ((self.lastname.lower(), self.firstname.lower()) >
                (other.lastname.lower(), other.firstname.lower()))
    def __ge__(self, other):
        print ((self.lastname.lower(), self.firstname.lower()),
                (other.lastname.lower(), other.firstname.lower())),
        return ((self.lastname.lower(), self.firstname.lower()) >=
                (other.lastname.lower(), other.firstname.lower()))
print dir(Student)

s1 = Student('lastname_1', 'firstname_3')
s2 = Student('lastname_3', 'firstname_3')

print 's1 == s2:\t', s1 == s2
print 's1 < s2:\t', s1 < s2
print 's1 > s2:\t', s1 > s2
print 's1 <= s2:\t', s1 <= s2
print 's1 >= s2:\t', s1 >= s2
