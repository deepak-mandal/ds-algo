#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:13:44 2020

@author: deepak
"""


class person:
    counter=0     #------------------------------------------------------------Class Attribute
    def __init__(self, a='Ravi', b='Ravi'):       #----------------------------Instance method or methods
        self.name=a           #------------------------------------------------Attributes or Instance Variables
        self.gender=b            #---------------------------------------------Attribute or Instance variable
        person.counter=person.counter+1
    def ShowInfo(self):           #--------------------------------------------Instance method or methods
        print('Name: ', self.name)
        print('Gender', self.gender)
    @classmethod
    def ShowCount(cls):         #----------------------------------------------Class method
        print('Number of object created so far: ', cls.counter)
        
