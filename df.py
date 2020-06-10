import pandas as pd
d = {'name':pd.Series(['Alisa','Bobby','Cat','madan','rocky','jocky','jack','rahul','david','ajay']),
   'age':pd.Series([26,27,28,19,64,65,14,58,25,12]),
   'score':pd.Series([89,87,90,96,99,70,71,45,54,58])}
df=pd.DataFrame(d)      #Creating Data frame
print(df)

print(df.describe())    #Getting Data summerisation such as mean, std etc.

