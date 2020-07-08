#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:01:33 2020

@author: deepak
"""

price=int(input('Enter the price of a donut: Rs '))
quantity=int(input('Enter the no. of donuts: '))
amount=price*quantity

if amount>1000:
    print('Yayy....a discount of 10% is applicable!')
    discount=amount*10/100
    amount=amount-discount
    
#if the amount is less than Rs. 1000, 5% discount is applicable

else: 
    print('A discount of 5% is applicable!')
    discount=amount*5/100
    amount=amount-discount

print('Your total amount is: Rs {}'.format(amount))