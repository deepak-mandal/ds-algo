#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 01:33:57 2020

@author: deepak
"""



#Horizontal Bar Chart
import matplotlib.pyplot as plt
import numpy as np
 
city=['Delhi','Beijing','Washington','Tokyo','Moscow']
pos = np.arange(len(city))
Happiness_Index=[60,40,70,65,85]
 
plt.barh(pos,Happiness_Index,color='blue',edgecolor='black')
plt.yticks(pos, city)
plt.xlabel('Happiness_Index', fontsize=16)
plt.ylabel('City', fontsize=16)
plt.title('Barchart - Happiness index across cities',fontsize=20)
plt.show()
