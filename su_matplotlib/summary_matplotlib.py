#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-15 11:17
# Author  : MrFiona
# File    : summary_matplotlib.py
# Software: PyCharm Community Editionz`


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24


x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)


plt.show()