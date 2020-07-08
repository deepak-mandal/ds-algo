#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:53:41 2020

@author: deepak
"""


#defining variables
day=0
squats=0
total=0
print('Enter the no. of squats you did on each day for the last one week .... and dont\'n lie!\n')        #Display instructions

#while loop and the loop body
while day<=6:
    day=day+1
    squats=int(input('Squats on Day {}: '.format(day)))
    total=total+squats
    

#statement outside of the while loop
avg=total/day
print('In the last {} days, you did an average of {} squats!'.format(day, avg))