import pandas as pd
 
print('data frame1: ')

d1 = {'Customer_id':pd.Series([1,2,3,4,5,6]),
      'Product':pd.Series(['Oven','Oven','Oven','Television','Television','Television'])}
df1 = pd.DataFrame(d1)
print(df1)

print('data frame2: ')
d2 = {'Customer_id':pd.Series([2,4,6]),
      'State':pd.Series(['California','California','Texas'])}
df2 = pd.DataFrame(d2)
print(df2)
print()

print('Inner join using pandas like SQL join: ')
print (pd.merge(df1, df2, on='Customer_id', how='inner'))
print()

print('Full join:')
print (pd.merge(df1, df2, on='Customer_id', how='outer'))
print()

print('Left Join:')
print(pd.merge(df1, df2, on='Customer_id', how='left'))
print()

print('Right Join: ')
print (pd.merge(df1, df2, on='Customer_id', how='right'))
