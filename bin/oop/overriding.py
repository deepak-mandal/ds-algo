#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:48:17 2020

@author: deepak
"""


#base class=Employee
#Sub class=SalesOfficer

class Employee:
    def __init__(self, nm, sal):
        self.name=nm
        self.salary=sal
        
    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary
    
    
class SalesOfficer(Employee):
    def __init__(self, nm, sal, inc):
        super().__init__(nm, sal)
        self.incnt=inc
        
    def getSalary(self):
        return self.salary+self.incnt


e1=Employee('Rajesh', 9000)
print('Total Salary for {} is Rs {} '.format(e1.getName(), e1.getSalary())) 
   
s1=SalesOfficer('kiran', 9000, 1000)
print('Total Salary for {} is Rs {} '.format(s1.getName(), s1.getSalary())) 
   
