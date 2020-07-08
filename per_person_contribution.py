#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:34:10 2020

@author: deepak
"""


#Calculate total contribution per person.
def food(f):
    #tip=0.1*f
    #f=f+tip
    fperson=f/num
    return fperson


def movies(m):
    return m/num

num=int(input('No.of friends: '))
ftotal=float(input('Spent on food: '))
mtotal=float(input('Spent on movies: '))

x=food(ftotal)
y=movies(mtotal)
print('The perperson total is: Rs. {:.2f}'.format(x+y))