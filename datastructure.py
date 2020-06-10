#string
str1='hellojavatpoint'     
str2='how are you'
print(str1[0:2])
print(str1[4])
print(str1*2)
print(str1+str2)

#lists is an array of heterogeneous element, mutable/editable
l=[1, 'hi', 'python', 2]
print(l[0:2])
print(l)
print(l+l)
print(l*3)

#Tuple is similar to list but, () & immutable
t=('hi', 'python', 2)
print(t[1:])
print(t[0:2])
print(t)
print(t+t)
print(type(t))

#Dictionary { key : value ...}  "keys:immutable &unique;but values can be changed" 
d={1:'jimmy', 2:'alex', 3:'jhon', 4:'mike'}
print('I st name is '+d[1])
print ('2nd name is '+d[4])
print(d)
print(d.keys())
print(d.values())

#Advanced
#list
shoplist=['apple','carrot','mango','banana']
shoplist
len(shoplist)

for item in shoplist:
    print(item)
    
    
shoplist.append('rice')
shoplist

#sort
shoplist.sort()
shoplist

#index/select
shoplist[0]
shoplist[0:4]

#delete items
del shoplist[0]
shoplist

#tuple
zoo=('python', 'lion','elephant','bird')
zoo
len(zoo)

#dictonary
student={'A101':'Abhinav', 'A102':'Rohit', 'A103':'rahul', 'A104':'karan'}
student
student['A103']
print('Name of the roll no. A103 is ', student['A103'])
del student['A104']
student
len(student)

for rollno, name in student.items():
    print('name of {} is {}'. format(rollno, name))
    
#Adding value
student['A105']='Hitesh'
student

#set are unordered collection of objects;mutable/editable ([]), but it always print in (alphabatical) order and unique(no duplicates), Imp.point is case sensetive
teamA=set(['india','england','australia', 'srilanka','india','ireland'])
teamA
teamB=set(['pakistan', 'south africa', 'bangladesh','ireland'])
teamB
'india' in teamA
'india' in teamB

teamA.add('china')
teamA                   #put in order
teamA.add('india')
teamA                   #No duplicates
teamA.remove('australia')
teamA



















