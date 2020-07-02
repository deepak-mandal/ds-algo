#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:21:46 2020

@author: deepak
"""

'''
count=10
while count!=0:
    print('Keep going, totla left: {}'.format(count))
    count=count-1
print('Done! Now switch arms.')
'''

'''
for num in range(5):
    print(num)
'''    

'''
for i in [5, 0]:   
    print(i+1)
'''

'''
sum=0
dict={1:100, 2:200, 3:300}
for k in dict.keys():
    print(k, dict.get(k))
'''


'''
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
'''


'''
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
'''



'''
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
'''


'''
price=int(input('Enter the price of the donuts : Rs. '))
quantity=int(input('Enter the no. of donuts: '))
amount=price*quantity

if amount>1000:
    print('yayy.... a discount of 10% is applicable!')
    discount=amount*10/100
    amount=amount-discount
print('Your total amount is : Rs {}'.format(amount))             
'''


'''
year=int(input('Enter year: '))

if year%100==0:
    print('Divisible by 100')
    if year%400==0:
        print('Divisible by 400')
        print('Year {} is a leap year'.format(year))
    else:
        print('not divisible by 400')
        print('Year {} is not a leap year!'.format(year))
else:
    if year%4==0:
        print('Divisible by 4')
        print('Year {} is a leap year!'.format(year))
    else:
        print('not divisible by 4')
        print('Year {} is not a leap year!'.format(year))
'''


'''
sum=0
dict={1:100, 2:200, 3:300}
print('Dict= {}'.format(dict))
print('dict.items() = {} '.format(dict.items()))
for k, v in dict.items():
    print(k, v)    
'''


'''
for num in range(1, 11):
    print(num)
print('End of the sequence')
'''


'''
#calculate factorial
num=int(input('Enter a number: '))
fact=1
for x in range(1, num+1):
    fact=fact*x
    print('fact= {} '.format(fact))
print('The factorial of {} is {}'.format(num, fact))
'''



'''
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
'''




'''
price=int(input('Enter the price of the donuts : Rs. '))
quantity=int(input('Enter the no. of donuts: '))
amount=price*quantity

if amount>1000:
    print('yayy.... a discount of 10% is applicable!')
    discount=amount*10/100
    amount=amount-discount
print('Your total amount is : Rs {}'.format(amount))         
'''


'''
for num in range(1, 5, 2):
    print(num)
'''



'''
price=50
quantity=5
amount=price*quantity
print('Price: {:d} Quantity: {:d} Amount: {:d}.'.format(price, quantity, amount))
'''


'''
num=float(input('Enter any number:'))
if num>0:
    print('This is a positive number')
elif num<0:
    print('This is a negative number')
else:
    print('This is neither negative nor positive, Hence it is zero.')
'''


'''
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
'''        



'''
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
'''



'''
#defining variables
day=0
squats=0
total=0
print('Enter the no. of squats you did on each day for the last one week .... and dont\'n lie!\n')        #Display instructions

#while loop and the loop body
while day<=6:
    day=day+1
    squats=int(input('Squats on Day {}: '.format(day)))
    total=total+squats
    

#statement outside of the while loop
avg=total/day
print('In the last {} days, you did an average of {} squats!'.format(day, avg))
'''



'''
donut=int(input('Do you have 0 donut or 1 donut?: '))
if donut ==1:
    print('Eat the donuts However...')
print('Less suger for you!')
'''

'''
dict={1:100, 2:200, 3:300}
for symbol in dict:
    print(symbol)
'''




'''
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
'''

'''
# String iteration 
for char in 'Push-ups':
    print(char)
print('Push-ups done!')
'''



'''
#Average of numbers in a list
total=0
numbers=[10, 20, 30, 40, 50]
for num in numbers:
    total=total+num
avg=total/len(numbers)
print('The average of given number is: ', avg)
'''


'''
#Print all key-value pairs in the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}

for country in capitals.items():
    print('The country and its capital are {}.'.format(country))
'''


'''
#print all key-value pairs in the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}
for country, city in capitals.items():
    print('The capitals of {} is {}.'.format(country, city))
'''


'''
#print all key-value pairs in the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}
for country in capitals.keys():
    print('The capitals of {} is {}.'.format(country, capitals.get(country)))
'''


'''
#print the key of the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}
for k in capitals.keys():
    print(k)
'''


'''
anyname=input('What is your name?')
print('Hello World! This is ', anyname)
'''


'''
a=input('enter any number')
b=input('Enter any number')
print(a+b)
'''


'''
# String iteration 
for char in 'Push-ups':
    print(char)
print('Push-ups done!')

'''

'''
#Average of numbers in a list
total=0
numbers=[10, 20, 30, 40, 50]
for num in numbers:
    total=total+num
avg=total/len(numbers)
print('The average of given number is: ', avg)
'''

'''
#Print all key-value pairs in the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}

for country in capitals.items():
    print('The country and its capital are {}.'.format(country))
'''

'''
#print all key-value pairs in the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}
for country, city in capitals.items():
    print('The capitals of {} is {}.'.format(country, city))
'''

'''
#print all key-value pairs in the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}
for country in capitals.keys():
    print('The capitals of {} is {}.'.format(country, capitals.get(country)))
'''

'''
#print the key of the dictionary
capitals={'USA':'New York', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi'}
for k in capitals.keys():
    print(k)
'''

'''
#else after 'for' iteration
for x in range(1, 5):
    print('This is iteration number {} in the \'for\' loop.'.format(x))
else:
    print('This is else block in the loop.')
print('Now, the loop ends!')
'''

'''
#else with the 'while' loop
x=0
while x<=5:
    x=x+1
    print('This is iteration number {} in the \'while\' loop.'.format(x+1))
else:
    print('This is else block in the loop.')
print('Now, the loop end!')
'''

'''
# print numbers in descending order from 15
num=15
while num>0:
    print('This is number {}.'.format(num))
    num=num-1
    if num==10:
        break
print('Let see what happen!')
'''
 

'''   
#Check for a PRIME NUMBER 
num=int(input('Enter a number: '))
for x in range(2, num):
    if num%x==0:
        print('{} is NOT a prime number.'.format(num))
        break
else:
    print('{} is a prime number.'.format(num))
'''



'''
#PRIME FACTOR CALACUATION
num=int(input('Enter a number: '))
d=2
while num>1:
    if num%d==0:
        print(d)
        num=num/d
        continue
    d=d+1
'''


'''
i=0
while i<4:
    print(i)
    i=i+1
    if i==2:
        break
else:
    print(0)
'''
























    
