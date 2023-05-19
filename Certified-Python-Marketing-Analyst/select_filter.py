import pandas as pd
#Create a DataFrame
d = {'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
           'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}
 
df = pd.DataFrame(d)
print(df)
print()
#print(df.iloc[:8,:])


print('View a column of the dataframe in pandas:')
#print(df['Name'])
#print()
print(df.loc[:,'Name'])

print('View two columns of the dataframe in pandas:')
#print(df[['Name','Score']])
#print()
print(df.loc[:, ['Name', 'Score']])

print('To View first two rows of the dataframe in pandas:')
#print(df[:2])
print(df.iloc[:2,])


#Filter
print('all rows where score greater than 70')  
print(df[df['Score'] > 70])
print()

print('print all the rows where score greater than 70 and less than 85')
print(df[(df['Score'] > 70) & (df['Score'] < 85)])
print()


#Select
print('select first 2 rows')
#print(df.iloc[:2])
# or
print(df.iloc[:2,])

print('to select 3rd to 5 th rows')
#print(df.iloc[2:5])
# or
print(df.iloc[3:6,])

print('select all rows starting from third row')
#print(df.iloc[2:])
# or
print(df.iloc[2:,])

#Select column by using column number in pandas with .iloc
print('Select first 2 columns: ')
print(df.iloc[:,:2])
print()

print('Select first and fourth columns: ')
print(df.iloc[:,[0,3]])
print()

#Select value by using row name and column name in pandas with .loc:
print('select value by row label and column label using loc')
print(df.loc[[1,2,3,4,5],['Name','Score']])
