#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:50:41 2020

@author: deepak
"""

import sqlite3
MySchool=sqlite3.connect('schooltest.db')
mysid=int(input('Enter ID: '))
myname=input('Enter name: ')
myhouse=int(input('Enter house: '))
mymarks=float(input('Enter marks: '))

#try block to catch exceptions
try:
    curschool=MySchool.cursor()
    curschool.execute('''insert into students (studentID, name, house, marks) values (?, ?, ?, ?);
                      ''', (mysid, myname, myhouse, mymarks))
    MySchool.commit()
    print('One record added successfully.')
    
#except block to handle exceptions
except:
    print('Error in operation.')
    MySchool.rollback()
    
MySchool.close()

