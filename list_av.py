#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:46:23 2020

@author: deepak
"""


#Average of numbers in a list
total=0
numbers=[10, 20, 30, 40, 50]
for num in numbers:
    total=total+num
avg=total/len(numbers)
print('The average of given number is: ', avg)