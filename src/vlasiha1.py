# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:49:47 2020

@author: sou
"""


import src.isfread as isfr
# import matplotlib
import matplotlib.pyplot as plt
# pathlib.WindowsPath

[t, ch1, head] = isfr.isfread("data\\tek0050CH1.ISF")
# [t2, ch2, head] = isfr.isfread("data\\tek0050CH2.ISF")
# [t3, ch3, head]    = isfr.isfread("data\\tek0050CH3.ISF")


line = plt.plot(t, ch1)
plt.show()
