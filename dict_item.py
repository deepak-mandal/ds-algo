#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:45:52 2020

@author: deepak
"""


#Print all key-value pairs in the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}

for country in capitals.items():
    print('The country and its capital are {}.'.format(country))