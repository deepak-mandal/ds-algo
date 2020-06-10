#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 17:59:18 2020

@author: deepak
"""

'''
Data Frame /Data Summary
Describe()- Used to get summary statistics in python.
Describe Function gives the mean, std and IQR values.
'''
 
import pandas as pd
 
#Create a Dictionary of series
d = {'Name':pd.Series(['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
                       'Rahul','David','Andrew','Ajay','Teresa']),
     'Age':pd.Series([26,27,25,24,31,27,25,33,42,32,51,47]),
     'Score':pd.Series([89,87,67,55,47,72,76,79,44,92,99,69])}
 
#Create a DataFrame
df = pd.DataFrame(d)
print (df)
print()

#Descriptive or Summary Statistic of the numeric columns:
#Summary statistics
print(df.describe())
print()

#Descriptive or Summary Statistic of the character columns:
#Summary statistics of character column
print(df.describe(include=['object']))
print()

#Descriptive or Summary Statistic of all the columns
#Summary statistics of character column
print(df.describe(include='all'))
