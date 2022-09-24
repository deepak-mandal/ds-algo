#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:48:18 2020

@author: deepak
"""

import sqlite3
MySchool=sqlite3.connect('schooltest.db')

#Accepting a name and retrieving the corresponding record

nm=input('Enter name: ')
sql="select * from students where name='"+nm+"';"
curschool=MySchool.cursor()
curschool.execute(sql)
record=curschool.fetchone()
print(record)

#Deleting the retrieved record
res=input('Do you want to delete this record?(Y/N)')
sql="delete from students where name='"+nm+"';"

if res=='Y':
    try:
        curschool.execute(sql)
        MySchool.commit()
        print('record deleted successfully')
    except:
        print('Error in update operation')
        MySchool.rollback()
        
MySchool.close()
