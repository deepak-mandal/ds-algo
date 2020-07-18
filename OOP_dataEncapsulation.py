#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:13:44 2020

@author: deepak
"""


class person:
    counter=0       #------------------------------------------------------class attribute
    def __init__(self, a, b):         #--------------------Instance methods/methods 
        self.name=a        #---------------------------------------------------Attributes/Instance variable
        self.gender=b      #--------------------------------------------Attributes/Instance variable
        person.counter=person.counter+1
    def ShowInfo(self):         #---------------------------------------Instance methods/methods
        print('Name: ', self.name)
        print('Gender: ', self.gender)
        print()
    @classmethod
    def ShowCount(cls):         #----------------------------------------------class method
        print('Number of objects created so far: ', cls.counter)
        print()
        
        
        
p1=person('Deepak', 'Male')
p2=person('Matt', 'Male')
p3=person('Sophie', 'Female')

person.ShowCount()
p1.ShowInfo()
p2.ShowInfo()
p3.ShowInfo()
