#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:30:44 2020

@author: deepak
"""


class car:
    def __init__(self, a=40):    #--------------------------------------instance methods
        self.set_speed(a)    #----------------------------------------------attribute/instance variable
    def get_speed(self):    #--------------------------------------instance methods/methods
        return self._speed
    def set_speed(self, a):   #---------------------------------instance methods
        if a<=0 or a>=160:
            print('Speed needs to between 0 to 160')
        else:
            self._speed=a
    
#c1=car()
#print(c1.set_speed(50))

