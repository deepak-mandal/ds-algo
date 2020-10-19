#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:28:04 2020

@author: deepak
"""

#Quadrilateral=Base Class
#Rectangle=Child Class

class Quadrilateral:
    def __init__(self, a, b, c, d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d
        
    def perimeter(self):
        p=self.side1+self.side2+self.side3+self.side4
        print('perimeter = ', p)
        
       
class Rectangle(Quadrilateral):
    def __init__(self, a, b, c=None, d=None):
        super().__init__(a, b, c, d)
        self.side3=self.side1
        self.side4=self.side2
        
        
       
        
       
r1=Rectangle(10, 20)
r1.perimeter()
