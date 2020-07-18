#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:49:01 2020

@author: deepak
"""


class Employee:
    
    def __init__(self):
        self.name='Kiran'
        self.salary=10000
    def __str__(self):
        return 'Name = '+self.name +' salary '+str(self.salary)
        
e1=Employee()
print(e1)
