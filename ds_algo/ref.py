#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:17:36 2020

@author: deepak
"""


#Finding reference to last node
p=self.start
while p.link is not None:
    p=p.link
    
    
    
    
#Finding reference to second last node
p=self.start
while p.link.link is not None:
    p=p.link
    
    
    
    
    
#Finding reference to a node with particular info
p=self.start
while p is not None:
    if p.info==x:
        break
    p=p.link
    
    
    
#Finding reference to predecessor of a node with particular info
p=self.start
while p.link is not None:
    if p.link.info==x:
        break
    p=p.link
    
    
    
#Finding reference to a node at a particular position 
p=self.start
i=1
while i<k and p is not None:
    p=p.link
    i+=1
    






