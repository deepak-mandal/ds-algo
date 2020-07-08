#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:28:39 2020

@author: deepak
"""


#using globals()
alpha=1
beta=2
gamma=3
print(globals())

globals()['gamma']=5
print(gamma)