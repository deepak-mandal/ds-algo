#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:37:21 2020

@author: deepak
"""
#String
str1 = 'hello javatpoint'   
str2 = ' how are you'
print (str1[0:2])
print (str1[4])
print (str1*2)
print (str1 + str2)

#Lists
l  = [1, 'hi', 'python', 2]  
print (l[3:])  
print (l[0:2])
print (l)
print (l + l) 
print (l * 3)

#Tuple
t  = ('hi', 'python', 2)  
print (t[1:])
print (t[0:2]) 
print (t)
print (t + t) 
print (t * 3)  
print (type(t))  

#Dictionary
d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}   
print("1st name is "+d[1])
print("2nd name is "+ d[4])
print (d)
print (d.keys())
print (d.values())

'''list(Advance)
ordered collection of items; sequence of items in a list
'''
shoplist =['apple','carrot','mango', 'banana']
shoplist
len(shoplist)


for item in shoplist:
    print(item, end =' ')

#add item to list
shoplist.append('rice')
shoplist

#sorting
shoplist.sort()  #inplace sort
shoplist

#index/select
shoplist[0]
shoplist[0:4]

#delete item
del shoplist[0]
shoplist

'''Tuple
Used to hold multiple object; similar to lists; less functionality than list
immutable - cannot modify- fast ; ( )
'''
zoo = ('python','lion','elephant','bird')
zoo
len(zoo)
languages = ('c', 'java', 'php')
languages

'''
Dictionary - like an addressbook. use of associate keys with values
key-value pairs { 'key1':value1, 'key2':value2} ;
'''

student = {'A101': 'Abhinav', 'A102': 'Rohit', 'A103':'Rahul', 'A104': 'Karan'}
student
student['A103']
print('Name of rollno A103 is ', student['A103'])
del student['A104']
student
len(student)

for rollno, name in student.items():
    print('name of {} is {} '.format(rollno, name) )

#adding a value
student['A104'] = 'Hitesh'
student


'''
Sets :- Sets are unordered collections of objects; ( [ , ])
and it will always print in alphabatical order and no dublication of object
'''
teamA = set(['india', 'england', 'australia','sri lanka','ireland'])
teamA
teamB = set(['pakistan', 'south africa','bangladesh','ireland'])
teamB

'india' in teamA
'india' in teamB

teamA.add('china')
teamA
teamA.add('india')
teamA
teamA.remove('australia')
teamA
