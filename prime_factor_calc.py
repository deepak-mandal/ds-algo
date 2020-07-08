#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:40:56 2020

@author: deepak
"""


#PRIME FACTOR CALACUATION
num=int(input('Enter a number: '))
d=2
while num>1:
    if num%d==0:
        print(d)
        num=num/d
        continue
    d=d+1