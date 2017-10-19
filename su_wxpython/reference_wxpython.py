#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017-10-20 00:45
# Author  : MrFiona
# File    : reference_wxpython.py
# Software: PyCharm Community Edition



import random
import wx

########################################################################
class TabPanel(wx.Panel):
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)

        # colors = ["red", "blue", "gray", "yellow", "green"]
        # self.SetBackgroundColour(random.choice(colors))
        # grid = wx.GridBagSizer(hgap=10, vgap=10)  # 行和列的间距是5像素

        wx_font = wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD)

        self.quote = wx.StaticText(self, label='Mail Server', pos=(100, 30))
        self.quote.SetFont(wx_font)
        self.quote.SetForegroundColour('blue')

        self.editname = wx.TextCtrl(self, pos=(280, 30), size=(250, 28))
        # grid.Add(self.editname, pos=(1, 1))

        self.quote_1 = wx.StaticText(self, label='Sender Email', pos=(100, 100))
        self.quote_1.SetFont(wx_font)
        self.quote_1.SetForegroundColour('blue')

        self.editname_1 = wx.TextCtrl(self, pos=(280, 100), size=(250, 28))

        self.quote_2 = wx.StaticText(self, label='Recipient Email', pos=(100, 170))
        self.quote_2.SetFont(wx_font)
        self.quote_2.SetForegroundColour('blue')

        self.editname_2 = wx.TextCtrl(self, pos=(280, 170), size=(250, 28))

        self.quote_3 = wx.StaticText(self, label='Send Email', pos=(100, 240))
        self.quote_3.SetFont(wx_font)
        self.quote_3.SetForegroundColour('blue')

        self.editname_3 = wx.TextCtrl(self, pos=(280, 240), size=(250, 28))


class TabPanel_1(wx.Panel):
    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent)
        #
        # colors = ["red", "blue", "gray", "yellow", "green"]
        # self.SetBackgroundColour(random.choice(colors))

        wx_font = wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD)

        self.quote = wx.StaticText(self, label='Retrieve Data', pos=(100, 30))
        self.quote.SetFont(wx_font)
        self.quote.SetForegroundColour('blue')

        self.sampleList = ['YES', 'NO']
        self.edithear = wx.ComboBox(self, pos=(350, 30), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_1 = wx.StaticText(self, label='Review Excel File', pos=(100, 100))
        self.quote_1.SetFont(wx_font)
        self.quote_1.SetForegroundColour('blue')

        self.edithear_1 = wx.ComboBox(self, pos=(350, 100), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_2 = wx.StaticText(self, label='Maximum Time', pos=(100, 170))
        self.quote_2.SetFont(wx_font)
        self.quote_2.SetForegroundColour('blue')

        self.editname_2 = wx.TextCtrl(self, pos=(350, 170), size=(200, -1))

        self.quote_22 = wx.StaticText(self, label='minute(s)', pos=(560, 170))
        self.quote_22.SetFont(wx_font)
        # self.quote_22.SetForegroundColour('blue')


########################################################################
class DemoFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY,"Notebook Tutorial",size=(700,500))
        panel = wx.Panel(self)
        self.tab_num = 3

        #todo Email配置界面
        # self.notebook = wx.Notebook(panel)
        # tabOne = TabPanel(self.notebook)
        # self.notebook.AddPage(tabOne, "Email")

        # tabTwo = TabPanel_1(self.notebook)
        # self.notebook.AddPage(tabTwo, "Retrieve/Review")

        # tabThree = TabPanel(self.notebook)
        # self.notebook.AddPage(tabThree, "Template")

        # tabFour = TabPanel(self.notebook)
        # self.notebook.AddPage(tabFour, "Chart")
        #
        # tabFive = TabPanel(self.notebook)
        # self.notebook.AddPage(tabFive, "Other Config")
        #
        # tabSix = TabPanel(self.notebook)
        # self.notebook.AddPage(tabSix, "Default")

        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(self.notebook, 1, wx.ALL|wx.EXPAND, 5)

        # btn = wx.Button(panel, label="Add Page")
        # btn.Bind(wx.EVT_BUTTON, self.addPage)
        # sizer.Add(btn)

        # panel.SetSizer(sizer)
        self.Layout()

        self.Show()

    #----------------------------------------------------------------------
    # def addPage(self, event):
    #     """"""
    #     new_tab = TabPanel(self.notebook)
    #     self.notebook.AddPage(new_tab, "Tab %s" % self.tab_num)
    #     self.tab_num += 1

#----------------------------------------------------------------------


class DemoFrame_1(wx.Frame):
    """
    Frame that holds all other widgets
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY,"Notebook Tutorial",size=(1500,1000))
        self.tab_num = 3
        # colors = ["red", "blue", "gray", "yellow", "green"]
        # colors = ["white"]
        # self.SetBackgroundColour(random.choice(colors))

        self.sampleList = ['YES', 'NO']

        # wx_font = wx.Font(12, wx.MODERN, wx.ITALIC, wx.BOLD)
        wx_font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.LIGHT)
        wx_font1 = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        wx_font2 = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.BOLD)
        wx_font3 = wx.Font(12, wx.SWISS, wx.SLANT, wx.BOLD)
        wx_font5 = wx.Font(12, wx.SCRIPT, wx.ITALIC, wx.BOLD)
        wx_font6 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.BOLD)
        wx_font7 = wx.Font(12, wx.TELETYPE, wx.NORMAL, wx.BOLD)
        #todo 邮件配置部分
        self.quote = wx.StaticText(self, label='Mail Server', pos=(30, 30))
        self.quote.SetFont(wx_font1)
        self.quote.SetForegroundColour('blue')
        self.editname = wx.TextCtrl(self, pos=(210, 30), size=(250, 28))
        # grid.Add(self.editname, pos=(1, 1))

        self.quote_1 = wx.StaticText(self, label='Sender Email', pos=(30, 80))
        self.quote_1.SetFont(wx_font2)
        self.quote_1.SetForegroundColour('blue')
        self.editname_1 = wx.TextCtrl(self, pos=(210, 80), size=(250, 28))

        self.quote_2 = wx.StaticText(self, label='Recipient Email', pos=(30, 130))
        self.quote_2.SetFont(wx_font3)
        self.quote_2.SetForegroundColour('blue')
        self.editname_2 = wx.TextCtrl(self, pos=(210, 130), size=(250, 28))

        self.quote_3 = wx.StaticText(self, label='Send Email', pos=(30, 180))
        self.quote_3.SetFont(wx_font5)
        self.quote_3.SetForegroundColour('blue')
        self.edithear_1 = wx.ComboBox(self, pos=(210, 180), size=(250, 28), choices=self.sampleList, style=wx.CB_DROPDOWN)
        # todo 邮件配置部分

        #todo 文件配置部分
        self.quote = wx.StaticText(self, label='Retrieve Data', pos=(500, 30))
        self.quote.SetFont(wx_font6)
        self.quote.SetForegroundColour('blue')
        self.edithear = wx.ComboBox(self, pos=(700, 30), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_11 = wx.StaticText(self, label='Review Excel File', pos=(500, 80))
        self.quote_11.SetFont(wx_font7)
        self.quote_11.SetForegroundColour('blue')
        self.edithear_11 = wx.ComboBox(self, pos=(700, 80), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_22 = wx.StaticText(self, label='Maximum Time', pos=(500, 130))
        self.quote_22.SetFont(wx_font)
        self.quote_22.SetForegroundColour('blue')
        self.editname_33 = wx.TextCtrl(self, pos=(700, 130), size=(200, -1))

        self.quote_22 = wx.StaticText(self, label='minute(s)', pos=(910, 130))
        self.quote_22.SetFont(wx_font)
        #todo 文件配置部分

        #todo 图标配置部分
        self.quote_1_1 = wx.StaticText(self, label='Software Change', pos=(30, 260))
        self.quote_1_1.SetFont(wx_font2)
        # self.quote_1_1.SetForegroundColour('blue')
        # self.quote_1_1.SetBackgroundColour('white')
        self.edithear_1_1 = wx.ComboBox(self, pos=(210, 260), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_1_2 = wx.StaticText(self, label='New Sighting', pos=(30, 310))
        self.quote_1_2.SetFont(wx_font2)
        # self.quote_1_2.SetForegroundColour('blue')
        # self.quote_1_2.SetBackgroundColour('blue')
        self.edithear_1_2 = wx.ComboBox(self, pos=(210, 310), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_1_3 = wx.StaticText(self, label='Existing Sighting', pos=(30, 360))
        self.quote_1_3.SetFont(wx_font2)
        # self.quote_1_3.SetForegroundColour('blue')
        # self.quote_1_3.SetBackgroundColour('blue')
        self.edithear_1_3 = wx.ComboBox(self, pos=(210, 360), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_1_4 = wx.StaticText(self, label='Closed Sighting', pos=(30, 410))
        self.quote_1_4.SetFont(wx_font2)
        # self.quote_1_4.SetForegroundColour('blue')
        # self.quote_1_4.SetBackgroundColour('blue')
        self.edithear_1_4 = wx.ComboBox(self, pos=(210, 410), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_1_5 = wx.StaticText(self, label='Total Sighting', pos=(30, 460))
        self.quote_1_5.SetFont(wx_font2)
        # self.quote_1_5.SetForegroundColour('blue')
        # self.quote_1_5.SetBackgroundColour('cyan')
        self.edithear_1_5 = wx.ComboBox(self, pos=(210, 460), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_1_6 = wx.StaticText(self, label='Saved Test Case', pos=(30, 510))
        self.quote_1_6.SetFont(wx_font2)
        # self.quote_1_6.SetForegroundColour('yellow')
        # self.quote_1_6.SetBackgroundColour('yellow')
        self.edithear_1_6 = wx.ComboBox(self, pos=(210, 510), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_1_7 = wx.StaticText(self, label='Saved Efforts', pos=(30, 560))
        self.quote_1_7.SetFont(wx_font2)
        # self.quote_1_7.SetForegroundColour('blue')
        # self.quote_1_7.SetBackgroundColour('grey')
        self.edithear_1_7 = wx.ComboBox(self, pos=(210, 560), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.quote_1_8 = wx.StaticText(self, label='Missed Sighting', pos=(30, 610))
        self.quote_1_8.SetFont(wx_font2)
        # self.quote_1_8.SetForegroundColour('blue')
        # self.quote_1_8.SetBackgroundColour('green')
        self.edithear_1_8 = wx.ComboBox(self, pos=(210, 610), size=(200, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        #todo 图标配置部分

        self.Layout()

        self.Show()



if __name__ == "__main__":
    app = wx.App(False)
    frame = DemoFrame_1()
    app.MainLoop()