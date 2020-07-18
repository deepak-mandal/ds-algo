#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:27:11 2020

@author: deepak
"""


import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
curschool.execute('''insert into students(syudentID, name, house, marks)
                  values (5, 'Sherlock', 32, 50);
                  
                  ''')
MySchool.commit()


