#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:41:36 2020

@author: deepak
"""


#Check for a PRIME NUMBER 
num=int(input('Enter a number: '))
for x in range(2, num):
    if num%x==0:
        print('{} is NOT a prime number.'.format(num))
        break
else:
    print('{} is a prime number.'.format(num))