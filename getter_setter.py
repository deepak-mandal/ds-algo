#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:30:44 2020

@author: deepak
"""


class car:
    def __init__(self, a=40):    #--------------------------------------instance methods
        self._speed=a    #----------------------------------------------attribute/instance variable
    def get_speed(self):    #--------------------------------------instance methods/methods
        return self._speed
    def set_speed(self, a):   #---------------------------------instance methods
        self._speed=a    #------------------------------------------------attribute/instance variables
        return
    
    
c1=car()
print(c1.get_speed())
print()
c1.set_speed(80)
print(c1.get_speed())

#c1.speed=60
#print(c1.speed)