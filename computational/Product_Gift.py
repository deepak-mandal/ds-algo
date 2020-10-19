#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:28:08 2020

@author: deepak
"""


class product:
    deliveryCharge=50
    def __init__(self, nam='Teddy Bear', prc=500):
        self.name=nam
        self.price=prc
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price+product.deliveryCharge
    
    def __str__(self):
        return print('The {} will cost you Rs {} '.format(self.get_name(), self.get_price()))
    
    
class gift(product):
    wrappingCharge=100
    def __init__(self, nam, prc):
        super().__init__(nam, prc)
        
    def get_price(self):
        return self.price+product.deliveryCharge+gift.wrappingCharge
    def __str__(self):
        return print('The {} will cost you Rs {} '.format(self.get_name(), self.get_price()))
    
    
product('A', 1 ).__str__()
gift('B', 1).__str__()
