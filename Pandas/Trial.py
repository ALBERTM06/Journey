import numpy as np
import pandas as pd

df = pd.read_csv('sample.csv',index_col = 'Name')

#Add employee
def add_employee():
    global df
    employee_name = input("Enter employee's name: ")
    if employee_name in df.index:
        print("Employee already exists!")
        return

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

#Search
def search_employee():
    employee_name = input("Enter employee's name: ")

    if employee_name in df.index:
        print(df.loc[employee_name])
    else:
        print("Employee not found")

#Delete employee
def delete_employee():
    global df
    employee_name = input("Enter employee's name: ")

    if employee_name in df.index:
        df.drop([employee_name], inplace=True)
        print("Employee details deleted successfully")
    else:
        print("Employee not found!")

#MAIN PROGRAM
print("Welcome to the Employee Management System!")

while True:
    print("Options: "
          "\n 1. Search Employee"
          "\n 2. Add New Employee"
          "\n 3. Delete Employee"
          "\n 4. Exit")
    try:
        option = int(input("Select one option to proceed: "))
    except ValueError:
        print("Enter valid number!")
        continue
    if option == 1:
        search_employee()
    elif option ==2:
        add_employee()
    elif option ==3:
        delete_employee()
    elif option ==4:
        print("Exiting program")
        break
    else:
        print("Invalid option!")

df.to_csv('sample.csv', index_label= 'Name')


