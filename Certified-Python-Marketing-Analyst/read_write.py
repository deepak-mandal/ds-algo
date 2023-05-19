# Reading CSV Files with Pandas:
import pandas as pd

df = pd.read_csv('/home/deepak/code/Mall_Customers.csv')
print(df)
print()

# Writing
df.to_csv('/home/deepak/code/Mall_Customers_copy.csv')


# Reading Excel Files
df1 = pd.read_excel('/home/deepak/code/Online_Retail_Store.xlsx')
print(df1)
# Writing since, it's huge data
df2 = pd.DataFrame(df1.iloc[:200, :])
print (df2)
df2.to_excel('/home/deepak/code/Online_Retail_Store_copy.xlsx')
