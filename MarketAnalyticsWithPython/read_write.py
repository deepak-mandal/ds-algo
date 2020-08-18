#-------------------------Reading & Writing data in Files----------------------
# Reading CSV Files with Pandas:
import pandas
df = pandas.read_csv('/home/deepak/analytics/Mall_Customers.csv')
print(df)

# Writing CSV Files with Pandas:
import pandas
df.to_csv('/home/deepak/analytics/Mall_Customers(1).csv')



# Reading Excel Files with Pandas
df = pandas.read_excel('/home/deepak/analytics/Online_Retail_Store.xlsx')
print(df)

# Writing Excel Files with Pandas 
df1 = pandas.DataFrame(df)
print (df1)
df1.to_excel('Online_Retail_Store(1).xlsx')