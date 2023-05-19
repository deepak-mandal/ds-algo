#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:17:22 2021

@author: deepak
"""

import pandas as pd 
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
