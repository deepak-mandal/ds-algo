#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 01:47:59 2020

@author: deepak
"""



#Histogram with bar Filled:
import matplotlib.pyplot as plt
 
values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,5, histtype='bar', align='mid', color='c', label='Test score Data',edgecolor='black')
#Argument histype=’bar’ plots the histogram in bar filled format.
plt.legend()
plt.title('Histogram of score')
plt.show()
