#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:17:50 2020

@author: deepak
"""

import sqlite3
MySchool=sqlite3.connect('schooltest.db')
sql='''select * from students;'''
curschool=MySchool.cursor()
curschool.execute(sql)
result=curschool.fetchall()
for record in result:
    print(record)
    
