#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 01:31:24 2020

@author: deepak
"""


#--------------------------Bar Chart-------------------------------------------
#Vertical Bar Chart
import matplotlib.pyplot as plt
import numpy as np
 
city=['Delhi','Beijing','Washington','Tokyo','Moscow']
pos = np.arange(len(city))
#Here, arange() function sets the x axis value.
Happiness_Index=[60,40,70,65,85]
 
plt.bar(pos,Happiness_Index,color='blue',edgecolor='black')
plt.xticks(pos, city)
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Barchart - Happiness index across cities',fontsize=20)
plt.show()