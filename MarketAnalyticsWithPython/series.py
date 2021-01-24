#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:44:14 2021

@author: deepak
"""

import pandas as pd
obj=pd.Series([1, 24, 34, 35, 23, 3, 2, 55])
print(obj)
print(obj.values)
print(obj.index)



sdata={'ohio': 35000, 'texas': 71000, 'oregon': 16000, 'utah': 5000}
print(sdata)
obj3=pd.Series(sdata)
print(obj3)
print()
states=['california', 'ohio', 'oregon', 'texas']
obj4=pd.Series(sdata, index=states)
print(obj4)
print()
print('isnull: ')
print(pd.isnull(obj4))
print()
print(obj4.isnull())
print()
print(obj4.isnull().sum())
print()
print(pd.notnull(obj4))
print()
print(obj4.notnull())
print('Critical series features:-')
print()
print(obj3)
print()
print(obj4)
print()
o9=(obj3+obj4)
print(o9)

print('----------------------------------------------------------')
obj4.name='Population'
obj4.index.name='state'
print(obj4)

obj=pd.Series([4, 7, -5, 3])
obj.index=['bob', 'steve', 'jeff', 'rayan']
print(obj)




#numpy
import numpy as np
import math
obj=pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj)
o1= (obj[obj>0])
print(o1)
o2=(obj*2)
print(o2)
o3=(np.exp(obj))
print(o3)



obj=pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(obj)
print(obj.values)
print(obj.index)
print(obj['a'])
