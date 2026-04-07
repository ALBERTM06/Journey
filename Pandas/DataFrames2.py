import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#Conditional selection
#print(df>0)
# bool_df = df>0
# print(bool_df)
# print(df[bool_df]) #or df[df>0]

#Advanced example
# bool_ser = df['W']>0 #Series that returns the rows where the values in W are greater than 0 in boolean form
# print(bool_ser)
# result = df[bool_ser] #Taking the dataframe from the series bool_ser
# print(result) #Omits C because its value in W is less than 0
# my_cols = ['X','Y']
# result_df = result[my_cols]
# print(result_df)
#Defining many variables like this takes up more and more memory over time

#The above can thus be shortened as follows:
result_df = df[df['W']>0][['X','Y']] #Stack commands
print(result_df)

#Conditional selection with multiple conditions
#For an 'and' operation
#example = df[(df['W']>0) & (df['Y']>1)] #We use the ampersand symbol not 'and'
# to combine the two conditionals and () to show clear distinction
#print(example)

#For an 'or' operation
#example2 = df[(df['W']>0) | (df['Y']>1)] #We use the '|' symbol not 'or'
# to combine the two conditionals

#How to reset index
#df.reset_index() #You call the .reset_index() method. It has in_place set to true so the original df remains unchanged
#The original indexes 'A' to 'E' become a column and  the new indexes range  from 0 to nth row

# How to set a column as an index
new_index = 'NBO MSA KMU NYE KIA'.split()
df['States'] = new_index
print(df)
print(df.set_index('States', inplace= True)) #You call the .set_index() method. Original remains unchanged

new_row = pd.DataFrame(randn(1,4), ['TUR'], ['W','X','Y','Z'])
df = pd.concat([df,new_row])
print(df)


