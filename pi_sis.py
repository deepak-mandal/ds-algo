#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:51:41 2020

@author: deepak
"""

def pi(amt):
    if amt<7000:
        print('Rs {} Ahem, can you rethink this number please?'.format(amt))
    elif amt>10000:
        print('Rs {} Wow sis! You are a queen.'.format(amt))
    else:
        print('Rs {} Cool, thanks sis! x rupees will certainly help.'.format(amt))
    return


sis=float(input('Please enter How much do you want to pay: Rs '))
pi(sis)