#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:01:04 2020

@author: deepak
"""


year=int(input('Enter year: '))

if year%100==0:
    print('Divisible by 100')
    if year%400==0:
        print('Divisible by 400')
        print('Year {} is a leap year'.format(year))
    else:
        print('not divisible by 400')
        print('Year {} is not a leap year!'.format(year))
else:
    if year%4==0:
        print('Divisible by 4')
        print('Year {} is a leap year!'.format(year))
    else:
        print('not divisible by 4')
        print('Year {} is not a leap year!'.format(year))