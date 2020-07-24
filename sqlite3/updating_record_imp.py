#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:21:34 2020

@author: deepak
"""

import sqlite3
MySchool=sqlite3.connect('schooltest.db')

#Take input of the name
nm=input('Enter name: ')
#Creating a string of select query to fetch the record
sql="select * from students where name='"+nm+"';"

#Executing query
curschool=MySchool.cursor()
curschool.execute(sql)
record=curschool.fetchone()
print(record)

m=float(input('Enter new marks: '))
sql="update students set marks='"+str(m)+"' where name='"+nm+"';"

try:
    curschool.execute(sql)
    MySchool.commit()
    print('record update successfully')
    
except:
    print('error in update operation')
    MySchool.rollback()
    
