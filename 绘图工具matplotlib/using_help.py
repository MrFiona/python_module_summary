#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-27 09:45
# Author  : MrFiona
# File    : using_help.py
# Software: PyCharm Community Edition




#todo 1、legend
"""

    ===>loc：int or string or pair of floats, default: ‘upper right’ 字符串文本框放置的位置，有如下定义：
            'best'         : 0, (only implemented for axes legends)
            'upper right'  : 1,
            'upper left'   : 2,
            'lower left'   : 3,
            'lower right'  : 4,
            'right'        : 5, (same as 'center right', for back-compatibility)
            'center left'  : 6,
            'center right' : 7,
            'lower center' : 8,
            'upper center' : 9,
            'center'       : 10,

    upper指上部，lower指底部，center指中间
    可以用数字指定也可以用相应的字符串指定位置

    ===>bbox_to_anchor：instance or tuple of floats 如将图列的右上角放在轴的中心
        loc='upper right', bbox_to_anchor=(0.5, 0.5)

    ===>fontsize： int or float or {‘xx-small’, ‘x-small’, ‘small’, ‘medium’, ‘large’, ‘x-large’, ‘xx-large’}
    控制图例的字体大小。 如果值是数值，则大小将以绝对字体大小为单位。 字符串值相对于当前默认字体大小。 此参数仅在未指定prop的情况下使用。

    ===>numpoints：None or int 创建图例中的marker，None则数量默认是一个

    ===>markerscale: None or int or float 图列marker的相对比例大小

    ===>markerfirst: bool 如果为True，图例marker将放置在图例标签的左侧。 如果为False，图例标记将放置在图例标签的右侧。默认值为True。

    ===>frameon: None or bool 控制图列是否在边框之内放置，默认是None相当于True即在边框之内放置

    ===>fancybox: None or bool 控制是否应该启用圆形边缘，默认是None相当于True启用，否则False则为方形边框

    ===>shadow：None or bool 图列边框是否含有阴影

    ===>facecolor与edgecolor 控制图例边框颜色

    ===>title：str or None 图列的标题

    ===>borderpad: float or None 图例中的字符串以及marker到边框的距离

    ===>labelspacing: float or None 指定title情况下图例字符串到title的距离

    ===>handlelength: float or None 控制图列中marker两边线的长度

    ===>handletextpad: float or None 控制图列中字符串文本到marker之间的距离

    ===>borderaxespad: float or None

"""



