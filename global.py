#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:29:14 2020

@author: deepak
"""


age=7
def a():
    global age
    age=12
    print('Age is: ', age)    
    return

a()
print('Age outside the function: ', age)