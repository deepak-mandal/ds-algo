#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:55:46 2020

@author: deepak
"""


price=int(input('Enter Price: Rs '))
qty=int(input('Enter quantity: '))
amount=price*qty
if amount>10000:
    print('A 10% discount is applicable!')
    discount=amount*10/100
    amount=amount-discount
else: 
    if amount>5000:
        print('A 5% discount is applicable! ')
        discount=amount*5/100
        amount=amount-discount
    else:
        if amount>2000:
            print('A 2% discount is applicable!')
            discount=amount*2/100
            amount=amount-discount
        else:
            if amount>1000:
                print('1% discount is applicable!')
                discount=amount*1/100
                amount=amount-discount
            else:
                print('no discount applicable!')
print('Amount payable: {}'.format(amount))