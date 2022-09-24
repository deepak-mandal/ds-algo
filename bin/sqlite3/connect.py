#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:15:11 2020

@author: deepak
"""

import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
curschool.execute('''create table students(studentID integer primary key autoincrement,
                                           name text(20) not null, house text, marks real);''')
MySchool.close()
