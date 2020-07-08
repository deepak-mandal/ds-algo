#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:58:38 2020

@author: deepak
"""

#calculate factorial
num=int(input('Enter a number: '))
fact=1
for x in range(1, num+1):
    fact=fact*x
    print('fact= {} '.format(fact))
print('The factorial of {} is {}'.format(num, fact))