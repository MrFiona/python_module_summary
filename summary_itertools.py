#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-09-01 18:51
# Author  : MrFiona
# File    : summary_itertools.py
# Software: PyCharm


"""
        Python-itertools模块小结
        itertools.count(start=0, step=1)
        itertools.cycle(iterable)
        itertools.repeat(object[, times])

        itertools.chain(*iterables)
        itertools.compress(data, selectors)
        itertools.dropwhile(predicate, iterable)
        itertools.groupby(iterable[, key])
        itertools.ifilter(predicate, iterable)
        itertools.ifilterfalse(predicate, iterable)
        itertools.islice(iterable, stop)
        itertools.imap(function, *iterables)
        itertools.starmap(function, iterable)
        itertools.tee(iterable[, n=2])
        itertools.takewhile(predicate, iterable)
        itertools.izip(*iterables)
        itertools.izip_longest(*iterables[, fillvalue])

        itertools.product(*iterables[, repeat])
        itertools.permutations(iterable[, r])
        itertools.combinations(iterable, r)
        itertools.combinations_with_replacement(iterable, r)
"""



import sys
import time
from operator import itemgetter
from collections import Iterator, Iterable
import itertools
import collections


# todo itertools.count(start=0, step=1) 返回包含结果的迭代器 元素为：start, start + step, start + step*2, .......
# todo 实现版本
def count(first_val=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    x = first_val
    while 1:
        yield x
        x += step

iter_count = itertools.count(0, 10)
print iter_count, type(iter_count), isinstance(iter_count, Iterator), isinstance(iter_count, Iterable)
print sys.maxint, sys.maxsize, sys.maxunicode
# for ele in iter_count:
#     print ele
#     if ele >= 20:
#         break
#     time.sleep(1)


# todo itertools.cycle(iterable) 创建一个迭代器，对iterable中的元素反复执行循环操作，内部会生成iterable中的元素的一个副本，此副本用于返回循环中的重复项
# todo example : itertools.cycle('ABCD') ---> A B C D A B C D .................
# todo 实现版本
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element

#todo 举例
index = 0
for item in itertools.cycle(['A', 'B', 'C', 'D']):
    index += 1
    if index > 10:
        break
    print (index, item)

# for ele in  itertools.cycle('123456'):
#     print ele
#     time.sleep(1)


# todo itertools.repeat(object[,times]) 创建一个迭代器，重复生成object，times（如果已提供）指定重复计数，如果未提供times，将无止尽返回该对象。
#todo 实现版本
def repeat(object, time=None):
    # repeat(10, 3) --> 10 10 10
    if time is None:
        while 1:
            yield object
    else:
        for i in xrange(time):
            yield object

#todo 举例
for item in itertools.repeat([1,2,3,4], 4):
    print item


# todo itertools.chain(*iterables) 将多个可迭代的对象作为参数, 但只返回单个迭代器, 将多个对象中的元素合并为一个迭代器内并返回
# todo chain类的方法，from_iterable(iterable)将iterable中的可迭代的元素放到一个迭代器中并返回 注意：元素必须是可迭代的否则会报错
#todo 实现版本
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for iterable in iterables:
        for ele in iterable:
            yield ele

# todo 举例
chain_list = [ element for element in itertools.chain([1, 2, 3, 4], itertools.repeat('D', 3)) ]
print chain_list
m = itertools.chain([1, 2, 3, 4], itertools.repeat('D', 3))
print m.from_iterable([11, 222, 'fff'])
chain_from_test = [ ele for ele in  m.from_iterable(['WWW', '2222', 'fff']) ]
print chain_from_test, type(chain_from_test)
for i in itertools.chain.from_iterable(['WWW', '2222', 'fff']):
    print i


# todo itertools.dropwhile(predicate, iterable) 创建一个迭代器，只要函数predicate(item)为True，就丢弃iterable中的项，如果predicate返回False，就会生成iterable中的项和所有后续项。
#todo 实现版本
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    # 返回第一个为False的项
    for item in iterable:
        if not predicate(item):
            yield item
            break
    # 返回第一个为False的项之后的所有项
    for x in iterable:
        yield x

#todo 举例
for i in itertools.dropwhile(lambda x: x<1, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i


# todo itertools.groupby(iterable[, key]) 返回一个产生按照key进行分组后的值集合的迭代器
#todo 实现版本
class groupby(object):
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def next(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))
    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)

#todo 举例
qs = [{'date' : 1},{'date' : 2}]
group_list = [(name, list(group)) for name, group in itertools.groupby(iterable=qs, key=lambda p:p['date'])]
print group_list
a = ['aa', 'ab', 'abc', 'bcd', 'abcde']
#按照元素长度分类
for i, k in itertools.groupby(iterable=a, key=len):
    print 'i=', i, '\tk=', list(k)

d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
di = sorted(d.iteritems(), key=itemgetter(1))
print d, di
for k, g in itertools.groupby(iterable=di, key=itemgetter(1)):
    print 'map(itemgetter(0),g)=', map(itemgetter(0),g), '\tk=', k, '\tg=', list(g)


# todo itertools.ifilter(predicate, iterable) 创建一个迭代器，仅生成iterable中predicate(item)为True的项，如果predicate为None，将返回iterable中所有计算为True的项, 类似于内置函数 filter()
#todo 实现版本
def ifilter(predicate, iterable):
    # ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
    if predicate is None:
        predicate = bool
    for item in iterable:
        if predicate(item):
            yield item

#todo 举例
for i in itertools.ifilter(lambda x: x<1, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i


# todo itertools.ifilterfalse(predicate, iterable) 和ifilter(函数相反 ， 返回一个包含那些测试函数返回false的项的迭代器)
#todo 实现版本
def ifilterfalse(predicate, iterable):
    # ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x

#todo 举例
for i in itertools.ifilter(lambda x: x<1, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i


# todo itertools.islice(iterable, stop) itertools.islice(iterable, start, stop[, step]) 返回序列seq的从start开始到stop结束的步长为step的元素的迭代器
#todo 实现版本
def islice(iterable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    it = iter(xrange(s.start or 0, s.stop or sys.maxint, s.step or 1))
    nexti = next(it)
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)

#todo 举例
print 'Stop at 5:',
for i in itertools.islice(itertools.count(1,10), 5):
    print i,

print 'Start at 5, Stop at 10:',
for i in itertools.islice(itertools.count(1,10), 5, 10):
    print i,

print 'By tens to 100:',
for i in itertools.islice(itertools.count(1,10), 0, 100, 10):
    print i,


#todo itertools.compress(data, selectors) takes two iterators and returns only those elements of data for which the corresponding element of selectors is true, stopping whenever either one is exhausted:
#todo 实现版本
def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    return (d for d, s in itertools.izip(data, selectors) if s)


#todo itertools.imap(function, *iterables) 返回序列每个元素被func执行后返回值的序列的迭代器
#todo 创建一个迭代器，生成项function(i1, i2, ..., iN)，其中i1，i2...iN分别来自迭代器iter1，iter2 ... iterN，如果function为None，则返回(i1, i2, ..., iN)形式的元组，只要提供的一个迭代器不再生成值，迭代就会停止。
#todo 即：返回一个迭代器, 它是调用了一个其值在输入迭代器上的函数, 返回结果. 它类似于内置函数 map() , 只是前者在任意输入迭代器结束后就停止(而不是插入None值来补全所有的输入).
#todo 实现版本
def imap(function, *iterables):
    # imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
    iterables = map(iter, iterables)
    while True:
        args = [next(it) for it in iterables]
        if function is None:
            yield tuple(args)
        else:
            yield function(*args)

#todo 举例
print 'Doubles:'
for i in itertools.imap(lambda x:2*x, xrange(5)):
    print i

print 'Multiples:'
for i in itertools.imap(lambda x,y:(x, y, x*y), xrange(5), xrange(5,10)):
    print '%d * %d = %d' % i


#todo itertools.starmap(function, iterable) 对序列seq的每个元素作为func的参数列表执行, 返回执行结果的迭代器
#todo 创建一个迭代器，生成值func(*item),其中item来自iterable，只有当iterable生成的项适用于这种调用函数的方式时，此函数才有效
#todo 实现版本
def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)

#todo 举例
values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
for i in itertools.starmap(lambda x,y:(x, y, x*y), values):
    print '%d * %d = %d' % i


#todo itertools.tee(iterable[, n=2]) 把一个迭代器分为n个迭代器, 返回一个元组.默认是两个
#todo 返回一些基于单个原始输入的独立迭代器(默认为2). 它和Unix上的tee工具有点语义相似, 也就是说它们都重复读取输入设备中的值并将值写入到一个命名文件和标准输出中
#todo 从iterable创建n个独立的迭代器，创建的迭代器以n元组的形式返回，n的默认值为2，此函数适用于任何可迭代的对象，但是，为了克隆原始迭代器，生成的项会被缓存，
#todo 并在所有新创建的迭代器中使用，一定要注意，不要在调用tee()之后使用原始迭代器iterable，否则缓存机制可能无法正确工作。

#todo 实现版本
def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                newval = next(it)       # fetch a new value and
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)

#todo 举例
r = itertools.islice(count(), 5)
i1, i2 = itertools.tee(r)

for i in i1:
    print 'i1:', i
for i in i2:
    print 'i2:', i


# todo itertools.takewhile(predicate, iterable) 创建一个迭代器，只要函数predicate(item)False，就丢弃iterable中的项，
#todo 如果predicate返回True，就会生成iterable中的项和所有后续项。
#todo 实现版本
def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break

#todo 举例
for i in itertools.takewhile(lambda x: x<2, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i


#todo itertools.izip(*iterables) 返回一个合并了多个迭代器为一个元组的迭代器. 它类似于内置函数zip(), 只是它返回的是一个迭代器而不是一个列表
#todo 创建一个迭代器，生成元组(i1, i2, ... iN)，其中i1，i2 ... iN 分别来自迭代器iter1，iter2 ... iterN，
#todo 只要提供的某个迭代器不再生成值，迭代就会停止，此函数生成的值与内置的zip()函数相同

#izip(iter1, iter2, ... iterN):
#返回:(it1[0],it2 [0], it3[0], ..), (it1[1], it2[1], it3[1], ..)...
#todo 实现版本
def izip(*iterables):
    # izip('ABCD', 'xy') --> Ax By
    iterators = map(iter, iterables)
    while iterators:
        yield tuple(map(next, iterators))

#todo 举例
for i in itertools.izip([1, 2, 3], ['a', 'b', 'c']):
    print i


#todo itertools.izip_longest(*iterables[, fillvalue]) 与izip()相同，但是迭代过程会持续到所有输入迭代变量iter1,iter2等都耗尽为止，
#todo 如果没有使用fillvalue关键字参数指定不同的值，默认使用None来填充已经使用的迭代变量的值。

#todo 实现版本
class ZipExhausted(Exception):
    pass

def izip_longest(*args, **kwds):
    # izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    fillvalue = kwds.get('fillvalue')
    counter = [len(args) - 1]
    def sentinel():
        if not counter[0]:
            raise ZipExhausted
        counter[0] -= 1
        yield fillvalue
    fillers = repeat(fillvalue)
    iterators = [chain(it, sentinel(), fillers) for it in args]
    try:
        while iterators:
            yield tuple(map(next, iterators))
    except ZipExhausted:
        pass

#todo 举例
for i in itertools.izip_longest([1, 2, 3], ['a', 'b', 'c', 5], fillvalue='default_link_string'):
    print i


#todo itertools.product(*iterables[, repeat]) 笛卡尔积 创建一个迭代器，生成表示item1，item2等中的项目的笛卡尔积的元组，
#todo repeat是一个关键字参数，指定重复生成序列的次数。

#todo 实现版本
def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111     (0,1) (0,1) (0,1) 组合 (0，1)重复三次
    pools = map(tuple, args) * kwds.get('repeat', 1)
    print 'pools:\t', pools
    result = [[]]
    for pool in pools:
        print 'pool:\t', pool
        result = [x+[y] for x in result for y in pool]
        print 'result:\t', result
    for prod in result:
        yield tuple(prod)

#todo 举例
a = (1, 2, 3)
b = ('A', 'B', 'C')
c = product(a,b)
for elem in c:
    print elem


#todo itertools.permutations(iterable[, r]) 排列 创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，
#todo 那么序列的长度与iterable中的项目数量相同： 返回p中任意取r个元素做排列的元组的迭代器

#todo 实现版本
def permutations_1(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210  r未指定则取range(3)中的3为r值
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

#todo 也可以用product实现
def permutations_2(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in itertools.product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


#todo itertools.combinations(iterable, r) 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 (不带重复)
#todo 实现版本
def combinations_1(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

#或者
def combinations_2(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


#todo itertools.combinations_with_replacement(iterable, r) 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 (带重复)
#todo 实现版本
def combinations_with_replacement_1(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

# 或者
def combinations_with_replacement_2(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
