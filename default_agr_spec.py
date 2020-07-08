#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:38:17 2020

@author: deepak
"""


#Do I have mony to splurge on the latest smartphone?
def verdict(m1, m2, m3, m4=15000):
    total=m1+m2+m3
    if total>=m4:
        print('Yes, you can get a new smartphone! But you should save this hard-earned money!\n')
    else:
        print('Sorry, this is not the right time to spurge on a smartphone.\n')
    return

gift=int(input('Gift money from family: Rs. '))
saving=int(input('Saving: Rs. '))
internship=int(input('Internship, earned with sweat and blood: Rs. '))
verdict(gift, saving, internship)