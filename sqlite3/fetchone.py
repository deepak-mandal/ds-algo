#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:06:43 2020

@author: deepak
"""

import sqlite3
MySchool=sqlite3.connect('schooltest.db')
sql='''select * from students;'''
curschool=MySchool.cursor()
curschool.execute(sql)

while True:
    record=curschool.fetchone()
    if record==None:
        break
    print(record)
    
    
