#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:02:51 2020

@author: deepak
"""


price=float(input('Enter Price: Rs '))
qty=int(input('Enter quantity: '))
amount=price*qty

if amount>10000:
    print('10% discount is applicable!')
    discount=amount*10/100
    amount=amount-discount
elif amount>5000:
    print('5% discount is applicable!')
    discount=amount*5/100
    amount=amount-discount
elif amount>2000:
    print('2% discount is applicable!')
    discount=amount*2/100
    amount=amount-discount
elif amount>1000:
    print('1% discount is applicable!')
    discount=amount*1/100
    amount=amount-discount
else:
    print('no discount is applicable!')
    
print('Amount payable: Rs {}'.format(amount))