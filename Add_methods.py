#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 12:05:41 2020

@author: deepak
"""

'''
d1='5 feet and 9 inches'
d2='6 feet and 11 inches'
d3=d1+d2
print(d3)
'''

class Distance:
    def __init__(self, x, y):
        self.feet=x
        self.inches=y
        
    def __add__(self, other):
        final_feet=self.feet+other.feet
        final_inches=self.inches+other.inches
        
        if final_inches>12:
            final_feet=final_feet+1
            final_inches=final_inches-12
        return Distance(final_feet, final_inches)
    
    def __str__(self):
        return 'Distance: '+str(self.feet)+' feet and '+str(self.inches)+' inches'
    
    
d1=Distance(9, 10)
d2=Distance(8, 9)
d3=d1+d2
print(d3)

















