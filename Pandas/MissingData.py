import numpy as np
import pandas as pd

#Creating a DataFrame with missing data from a dictionary
d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
#print(df)

#Deleting/Dropping missing data
#print(df.dropna())

#Dropping columns with missing data
#print(df.dropna(axis = 1))

#You can choose to set a threshold for what to drop
#print(df.dropna(thresh = 2)) #Drops rows with 2 missing values and leaves the row with <2 missing values

#Filling missing data by setting the value - Typically filled with strings or the mean of respective columns
print(df)
print(df.fillna(value = 'FILL VALUE'))
print(df.loc[1].fillna(value = df.loc[1].mean()))