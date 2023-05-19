import pandas as pd
 
d = {'Name':['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
                       'Rahul','David','Andrew','Ajay','Teresa'],
'Age':[26,27,25,24,31,27,25,33,42,32,51,47],
'Score':[89,87,67,55,47,72,76,79,44,92,99,69]}
 
#creating Dataframe from dict or Series
df = pd.DataFrame(d)
print (df)
print()
#Summary statistics
print(df.describe())
