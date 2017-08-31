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


