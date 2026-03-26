import numpy as np
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,333,444,],
                   'col3':['abc','def','ghi','jkl']})
df.head()
print(df)

#Info on unique values
# print(df['col2'].unique())
# print(df['col2'].nunique())
# print(df['col2'].value_counts())

#Selecting data
#new_df = df[(df['col1']>2) & (df['col2'] == 444)]
#print(new_df)

#Applying Functions
#User-defined function:
# def times2(x):
#     return x*2
#
# print(df['col1'].apply(times2))
#You can always use a lambda expression for the above as follows:
#print(df['col1'].apply(lambda x : x*2))

#Built-in functions can be applied as well
#print(df['col3'].apply(len))

#Dropping a column
#print(df.drop('col1', axis = 1))

#Get column and index names:
# print(df.columns)
# print(df.index)

#Sorting values
#print(df.sort_values(by='col2'))

#Find Null Values or Check for Null Values
print(df.isnull())
# Drop rows with NaN Values
print(df.dropna())

#Filling in NaN values with something else
df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()
df.fillna('FILL')

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)
print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))


