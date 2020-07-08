#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 02:09:08 2020

@author: deepak
"""


#-------------------------Reading & Writing data in Files----------------------
# Reading CSV Files with Pandas:
import pandas
df = pandas.read_csv('/home/deepak/Desktop/CPMA/data/50startups.csv')
print(df)







# Writing CSV Files with Pandas:
import pandas
df.to_csv('/home/deepak/Desktop/CPMA/data/50startups1.csv')






# Reading Excel Files with Pandas
df = pandas.read_excel('/home/deepak/Desktop/CPMA/data/Online_Retail_Store.xlsx')
print(df)






# Writing Excel Files with Pandas 
df1 = pandas.DataFrame(df)
print (df1)
df1.to_excel('/home/deepak/Desktop/CPMA/data/Online_Retail_Store1.xlsx')
