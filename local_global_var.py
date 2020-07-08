#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:27:32 2020

@author: deepak
"""


age=7
def a():
    print('Global variable \'age\': ', globals()['age'])
    #Now modifying the Global variable 'age' Inside the function
    globals()['age']=27
    print('Global variable \'age\' modified inside the function.', globals()['age'])
    #Now creating a local variable, 'age' inside the function
    age=11
    print('local variable \'age\' : ', age)
    return
a()
print('Checking global variable value outside the function: ', age)