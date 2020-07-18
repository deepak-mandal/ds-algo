#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:49:01 2020

@author: deepak
"""


class Employee:
    def __new__(cls):
        print('__new__ magic method is executed.')
        inst=object.__new__(cls)
        return inst
    def __init__(self):
        print('__init__ magic method is executed.')
        self.name='Kiran'
        
e1=Employee()
print(e1.name)
