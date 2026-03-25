import numpy as np
import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

#Other methods alongside GroupBy
#print(df.groupby('Company').max()) #Is a bit confusing because max data for Person picks the lexicographical max value
#So The max value for person is not its actual value in the data. Use .idxmax() instead to get the index of the max sale per company
#print(df.loc[df.groupby('Company')['Sales'].idxmax()])

# print(df.groupby('Company').count())
# print(df.groupby('Company')['Sales'].mean())
#print(df.groupby('Company')['Sales'].std())
#print(df.loc[df.groupby('Company')['Sales'].idxmin()])
#print(df.groupby('Company').describe().transpose())



