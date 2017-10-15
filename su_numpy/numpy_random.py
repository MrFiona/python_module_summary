#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-15 22:40
# Author  : MrFiona
# File    : numpy_random.py
# Software: PyCharm Community Edition


import numpy as np


rand_array = np.random.rand(2, 3)
print '\033[32mrand_array:\033[0m', rand_array

randn_array = np.random.randn(2, 3)
print '\033[33mrandn_array:\033[0m', randn_array

randn_array_signal = np.random.randn()
print '\033[33mrandn_array_signal:\033[0m', randn_array_signal

randint_array = np.random.randint(1, 10, size=(2, 3))
print '\033[34mrandint_array:\033[0m', randint_array
randint_array_signal = np.random.randint(1, 10)
print '\033[34mrandint_array_signal:\033[0m', randint_array_signal

random_integers_signal = np.random.random_integers(1, 100, 10)
print '\033[35mrandom_integers_signal:\033[0m', random_integers_signal
random_integers = np.random.random_integers(1, 10, size=(2,3))
print '\033[35mrandom_integers:\033[0m', random_integers

sample_array =  np.random.sample((3,))
sample_array_1 =  np.random.sample((3,2))
print '\033[36msample_array:\033[0m', sample_array
print '\033[36msample_array_1:\033[0m', sample_array_1
sample_array_signal =  np.random.sample()
print '\033[36msample_array_signal:\033[0m', sample_array_signal

random_signal =  np.random.random()
random =  np.random.random((2, 3))
print '\033[32mrandom:\033[0m', random_signal, random

ranf_signal =  np.random.ranf()
ranf_array =  np.random.ranf((2, 3))
print '\033[35mranf:\033[0m', ranf_signal, ranf_array

random_sample_signal = np.random.random_sample()
random_sample_array = np.random.random_sample((2, 3))
print '\033[31mrandom_sample:\033[0m', random_sample_signal, random_sample_array




