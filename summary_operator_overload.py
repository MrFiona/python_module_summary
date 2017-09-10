#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-09-09 22:06
# Author  : MrFiona
# File    : summary_operator_overload.py
# Software: PyCharm

"""

常用的运算符重载方法
    方法                      重载                     调用
    __init__                构造函数                   对象建立：X = Class(args)
    __del__                 析构函数                   X对象收回
    __add__                 运算符+                    如果没有_iadd_，X + Y , X += Y
    __or__                  运算符|（位OR）            如果没有_ior__，X | Y，X |= Y
    __repr__,__str__        打印、转换                 print(X)、repr(X)、str(X)
    __call__                函数调用                   X(*args, **kwargs)
    __getattr__             点号运算                   X.undefined
    __setattr__             属性赋值语句               X.any = value
    __delattr__             属性删除                   del X.any
    __getattribute__        属性获取                   X.any
    __getitem__             索引运算                   X[key],X[i:j],没__iter__时的for循环和其他迭代器
    __setitem__             索引赋值运算               X[key] = value,X[i:j] = sequence
    __delitem__             索引和分片删除             del X[key],del X[i:j]
    __len__                 长度                       len(X),如果没有__bool__,真值测试
    __bool__                布尔测试                   bool(X),真测试（在python2.6中叫__nonzero__）
    __lt__,__gt__,           特定的比较                X < Y,X>Y,X<=Y,X>=Y,
    __le__,__ge__,                                     X == Y, X != Y(或者在python2.6中
    __eq__,__ne__                                      只有__cmp__)
    __radd__                右侧加法                   Other + X
    __iadd__                实地（增强的）加法         X += Y(or else __add__)
    __iter__,__next__       迭代环境                   I = iter(X),next(I);for loops, in if no __contains__, all comprehensions, map(F,X),其他(__next__在python2.6中称为next)
    __contains__            成员关系测试               item in X（任何可迭代的）
    __index__               整数值                     hex(X),bin(X),oct(X),O[X],O[X:](替代python2中的__oct__, __hex__)
    __enter__,__exit__      环境管理器                with obj as var：
    __get__,__set__         描述符获取                X.attr,X.attr = value,del X.attr
    __delete__
    __new__                                           在__init__之前创建对象


     """


from collections import OrderedDict


class TestOperatorOverload(object):
    def __init__(self, val):
        self.var = val
        self._fee = None
        self.dict = OrderedDict()
        print 'this is __init__ func.\targs:\t', val

    def __abs__(self):
        print 'this is __abs__ func.'

    def __add__(self, other):
        print 'add:\t', 'var = ', self.var, 'other = ', other, 'type(other):\t', type(other)
        if isinstance(other, TestOperatorOverload):
            other = other.var
            result = TestOperatorOverload(self.var + other)
            return result, result.var, type(result)
        else:
            return self.var + other

    def __getitem__(self, item):
        print 'this is __getitem__ func.'
        return self.dict[item]

    def __setitem__(self, key, value):
        print 'this is __setitem__ func.'
        self.dict[key] = value

# todo 用普通方法将类方法转变为类属性
    def set_key(self, value):
        print 'set_key: self._x = ', value
        self._x = value

    def get_value(self):
        print 'get_value: ', self._x
        return self._x

    def del_x(self):
        print 'del _x'
        del self._x

    x = property(get_value, set_key, del_x, 'this is the x property!!!')
# todo 用普通方法将类方法转变为类属性

# todo 用内置属性装饰器property将类方法转变为类属性
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value

    @fee.deleter
    def fee(self):
        del self._fee
# todo 用内置属性装饰器property将类方法转变为类属性


class TestStrAndRepr:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return '(TestStrAndRepr: %s, %s)' % (self.name, self.address)

    #todo 简单的方式定义__repr__ 或者单独定义__repr__
    __repr__ = __str__


if __name__ == '__main__':
    test1 = TestOperatorOverload(123)
    test2 = TestOperatorOverload(32)
    m = test1 + 12
    m1 = test2 + 100
    print 'm:\t', m
    print 'm1:\t', m1
    print 'test2 + test1:\t', test2 + test1
    test1.set_key('test value')
    print test1.get_value()
    test1.del_x()

    test1.fee = 'fee helqwereg'
    print test1.fee

    test1['set'] = 'value'
    print test1['set']

    test3 = TestStrAndRepr('Bob', '西安')
    print test3

