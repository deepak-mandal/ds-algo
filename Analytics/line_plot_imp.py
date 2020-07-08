#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 01:05:23 2020

@author: deepak
"""


#Multiple Line charts with legends and Labels:
#lets take an example of sale of units in 2016 and 2017 to demonstrate line charts.
import matplotlib.pyplot as plt
sales1 = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
sales2 = [3, 7, 9, 6, 4, 5, 14, 7, 6, 16, 12]
line_chart1 = plt.plot(range(1,12), sales1)
line_chart2 = plt.plot(range(1,12), sales2)
plt.title('Monthly sales of 2016 and 2017')
plt.xlabel('Sales')
plt.ylabel('Month')
plt.legend(['year 2016', 'year 2017'], loc=4)
plt.show()