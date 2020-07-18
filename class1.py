#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:06:15 2020

@author: deepak
"""



class person:
    def __init__(self, a, b):
        self.name=a
        self.gender=b
    def ShowInfo(self):
        print('Name: ', self.name)
        print('Gender: ', self.gender)
        
     
p1=person('Sophie', 'Female')
p2=person('Mark', 'Male')

p1.ShowInfo()
p2.ShowInfo()


