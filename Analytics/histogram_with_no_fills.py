#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 01:45:46 2020

@author: deepak
"""


#--------------------------Histogram-------------------------------------------
#Histogram with no Fills:
import matplotlib.pyplot as plt
 
values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,5, histtype='step', align='mid', color='g', label='Test Score Data')
#Here, second argument is the number of bins, histype=’step’ which plots the histogram in step 
#format, aligned to mid, color chosen is green.
plt.legend(loc=2)
#argument loc=2 plots the legend on the top left corner.
plt.title('Histogram of score')
plt.show()