#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:35:06 2020

@author: deepak
"""

import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
curschool.execute('''insert into students(studentID, name, house, marks) values (5, 'sherlock', 32, 50);''')
MySchool.commit()
