import numpy as np
import pandas as pd
from numpy.random import randn

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
#print(df)

#Naming the index groups
df.index.names = ['Groups','Num']
#print(df)

#Selecting the groups
#print(df.loc['G1'])

#Selecting specific cells
#print(df)
#print(df.loc['G1'].loc[3,'A'])

#Selecting using .xs() which allows you to select cells from different groups
print(df.xs(1, level = 'Num'))


