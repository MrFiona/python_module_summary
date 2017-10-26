#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-26 13:08
# Author  : MrFiona
# File    : summary_pyplot.py
# Software: PyCharm Community Edition


import numpy as np
import matplotlib.pyplot as plt



plt.figure()

x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)
print x
line, = plt.plot(x, y, color='red', linestyle='-.', marker='o', markerfacecolor='m', markersize=8.40, label='label line', fillstyle='bottom'
         ,drawstyle='default', dash_capstyle='butt', dash_joinstyle='bevel', clip_on=False, antialiased=False, animated=False, alpha=0.5)
line.set_label('update label')
# plt.legend(['A simple line'])
plt.legend((line,),('A simple line',), loc='upper right', fontsize='medium', markerfirst=True, facecolor='green', edgecolor='magenta'
           ,title='title', borderpad=0.5, labelspacing=0.1, handlelength=3.0, handletextpad=1.0, borderaxespad=1.0, )
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Make some fake data.
a = b = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')

legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.show()



import matplotlib.pyplot as plt
# plot a line, implicitly creating a subplot(111)
plt.plot([1,2,3])
# now create a subplot which represents the top plot of a grid
# with 2 rows and 1 column. Since this subplot will overlap the
# first, the plot (and its axes) previously created, will be removed
plt.subplot(211)
plt.plot(range(12))
plt.subplot(212, facecolor='y') # creates 2nd subplot with yellow background
plt.show()