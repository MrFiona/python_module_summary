#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2018-07-22 02:20
# Author  : MrFiona
# File    : redis_summary.py
# Software: PyCharm



import redis

# todo 1、第一种连接方式
# 连接redis，加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='qq08061635', db=0, decode_responses=True)
r = redis.Redis(connection_pool=pool)
print(r.set('test', 'value'))

# todo 1、第二种连接方式
# r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='qq08061635', decode_responses=True)
# print(r.set('test', 'value'))


"""
    1、redis基本命令 String

    (1) set(name, value, ex=None, px=None, nx=False, xx=False)
        在Redis中设置值，默认，不存在则创建，存在则修改
        参数：
            ex，过期时间（秒）
            px，过期时间（毫秒）
            nx，如果设置为True，则只有name不存在时，当前set操作才执行
            xx，如果设置为True，则只有name存在时，当前set操作才执行

    (2) setnx(name, value) 
        只有name不存在时，执行设置操作（添加）

    (3) setex(name, value, time)
        参数：
        time，过期时间（数字秒 或 timedelta对象）

    (4) psetex(name, time_ms, value)
        参数：
        time_ms，过期时间（数字毫秒 或 timedelta对象）

    (5) mset(*args, **kwargs)
        批量设置值

    (6) mget(keys, *args)
        批量获取

    (7) getset(name, value)
        设置新值并获取原来的值

    (8) getrange(key, start, end)
        获取子序列（根据字节获取，非字符）
        参数：
            name，Redis 的 name
            start，起始位置（字节）
            end，结束位置（字节）
            如： "君惜大大" ，0-3表示 "君"

    (9) setrange(name, offset, value)
        修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
        参数：
            offset，字符串的索引，字节（一个汉字三个字节）
            value，要设置的值

    其他详情请见:https://www.jianshu.com/p/2639549bedc8
"""

# todo 1.ex，过期时间（秒） 这里过期时间是3秒，3秒后p，键food的值就变成None
r.set('food1', 'mutton', ex=3)  # key是"food" value是"mutton" 将键值对存入redis缓存， 过期时间是3秒，3秒后键food不存在
print(r.get('food1'))  # mutton 取出键food对应的值

# todo 2.px，过期时间（豪秒） 这里过期时间是3豪秒，3毫秒后，键foo的值就变成None
r.set('food2', 'beef', px=3)
print(r.get('food2'))

# todo 3.nx，如果设置为True，则只有name不存在时，当前set操作才执行 （新建）
print(r.set('fruit', 'watermelon', nx=True))  # True--不存在
# 如果键fruit不存在，那么输出是True；如果键fruit已经存在，输出是None

# todo 4.xx，如果设置为True，则只有name存在时，当前set操作才执行 （修改）
print((r.set('fruit', 'watermelon1', xx=True)))  # True--已经存在
# 如果键fruit已经存在，那么输出是True；如果键fruit不存在，输出是None

# todo
print(r.setnx('fruit1', 'banana'))  # fruit1不存在，输出为True

# print(r.mset(k='eee', m='wrrr'))
print(r.mset({'k1': 'v1', 'k2': 'v2'}))  # 这里k1 和k2 不能带引号 一次设置对个键值对
print(r.mget("k1", "k2"))  # 一次取出多个键对应的值
print(r.mget("k1"))

r.hmset("hash2", {"k3": "v3", "k4": "v4"})
print(r.hget("hash2", "k3"))  # 单个取出"hash2"的key-k3对应的value
print(r.hmget("hash2", "k3", "k4"))  # 批量取出"hash2"的key-k3 k4对应的value --方式1
print(r.hmget("hash2", ["k3", "k4"]))  # 批量取出"hash2"的key-k3 k4对应的value --方式2
print(r.hgetall("hash2"), type(r.hgetall("hash2")))

r.set('name', {'k1': '1000', 'k2': '2000'})

r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素
print(r.scard("set1"))  # 集合的长度是4
print(r.smembers("set1"))  # 获取集合中所有的成员

print(r.delete("m"))  # 删除key为gender的键值对

print(r.exists("set1"))  # 检测redis的name是否存在，存在就是True，False 不存在

print(r.keys("k*"))  # 根据模糊匹配获取redis的name

print(r.type("set1"))
print(r.type("hash2"))
print(r.type("k"))
print(r.type("name"))

# todo 管道（pipeline）
"""
    redis默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
    如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。

    管道（pipeline）是redis在提供单个请求中缓冲多条服务器命令的基类的子类。它通过减少服务器-客户端之间反复的TCP数据库包，从而大大提高了执行批量命令的功能。

"""

# pipe = r.pipeline(transaction=False)    # 默认的情况下，管道里执行的命令可以保证执行的原子性，执行pipe = r.pipeline(transaction=False)可以禁用这一特性。
# pipe = r.pipeline(transaction=True)
pipe = r.pipeline()  # 创建一个管道

pipe.set('name', 'jack')
pipe.set('role', 'sb')
pipe.sadd('faz', 'baz')
pipe.incr('num')  # 如果num不存在则vaule为1，如果存在，则value自增1
pipe.execute()

print(r.get("name"))
print(r.get("role"))
print(r.get("num"))

# 管道的命令可以写在一起
pipe.set('hello1', 'redis').sadd('faz1', 'baz').incr('num1').execute()
print(r.get("name1"))
print(r.get("role1"))
print(r.get("num1"))