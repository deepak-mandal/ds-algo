#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:57:55 2020

@author: deepak
"""


price=int(input('Enter the price of the donuts : Rs. '))
quantity=int(input('Enter the no. of donuts: '))
amount=price*quantity

if amount>1000:
    print('yayy.... a discount of 10% is applicable!')
    discount=amount*10/100
    amount=amount-discount
print('Your total amount is : Rs {}'.format(amount))    