import numpy as np
import pandas as pd

#CSV Input
# df = pd.read_csv('example.csv')
# print(df)
#df = pd.read_csv('sample.csv')
#print(df.to_string())

#Excel Input
# pd.read_excel('Excel_Sample.xlsx',sheet_name = 'Sheet1')
# df.to_excel('Excel_Sample2.xlsx', sheet_name = 'NewSheet')

#HTML Input
# df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# df[0].head()

#SQL
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:')
# df.to_sql('data', engine)
# sql_df = pd.read_sql('data',con=engine)
# print(sql_df)

#JSON files
df = pd.read_json('json_sample.json')
print(df.to_string())