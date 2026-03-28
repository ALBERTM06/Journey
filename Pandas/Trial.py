import numpy as np
import pandas as pd

df = pd.read_csv('sample.csv',index_col = 'Name')
print(df.to_string())

employee_name = input("Enter employee's name: ")
#Search
def search_employee():
    if employee_name in df.index:
        print(df.loc[employee_name])
    else:
        print("Employee not found")
        add_employee()

def add_employee():
    global df
    employee_email = input("Enter employee's email: ")
    employee_phone = input("Enter employee's phone: ")
    employee_city = input("Enter employee's city: ")

    new_row = pd.DataFrame({
        'Email': [employee_email],
        'Phone Number':[employee_phone],
        'City': [employee_city]
    }, index=[employee_name])
    df = pd.concat([df, new_row])
    print("\n Updated Data: ")
    print(df)




