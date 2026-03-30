import numpy as np
import pandas as pd

df = pd.read_csv('kinderland_inventory.csv', index_col='Product')


# View full inventory
def view_inventory():
    if df.empty:
        print("No products in inventory.")
        return
    print("\nCurrent Inventory:")
    print(df.to_string())
    print(f"\nTotal products: {len(df)}")
    print(f"Total stock units: {df['Stock'].sum()}")
    print(f"Estimated inventory value: KES {(df['Price (KES)'] * df['Stock']).sum():,.0f}")


# Search for a product
def search_product():
    name = input("Enter product name: ")
    if name in df.index:
        print(f"\n{name}:")
        print(df.loc[name])
    else:
        print("Product not found.")


# Add a new product
def add_product():
    global df
    name = input("Enter product name: ")
    if name in df.index:
        print("Product already exists. Use 'Update' to edit it.")
        return

    category = input("Enter category: ")

    try:
        price = float(input("Enter price (KES): "))
        stock = int(input("Enter stock quantity: "))
    except ValueError:
        print("Price and stock must be numbers.")
        return

    description = input("Enter short description: ")

    new_row = pd.DataFrame({
        'Category':     [category],
        'Price (KES)':  [price],
        'Stock':        [stock],
        'Description':  [description]
    }, index=[name])

    df = pd.concat([df, new_row])
    print(f"\n'{name}' added successfully.")


# Update stock or price for an existing product
def update_product():
    global df
    name = input("Enter product name: ")
    if name not in df.index:
        print("Product not found.")
        return

    print(f"\nCurrent details for '{name}':")
    print(df.loc[name])

    print("\nWhat would you like to update?"
          "\n 1. Price"
          "\n 2. Stock"
          "\n 3. Both")
    try:
        choice = int(input("Select option: "))
    except ValueError:
        print("Enter a valid number.")
        return

    if choice in [1, 3]:
        try:
            new_price = float(input("Enter new price (KES): "))
            df.loc[name, 'Price (KES)'] = new_price
        except ValueError:
            print("Invalid price.")
            return

    if choice in [2, 3]:
        try:
            new_stock = int(input("Enter new stock quantity: "))
            df.loc[name, 'Stock'] = new_stock
        except ValueError:
            print("Invalid stock quantity.")
            return

    print(f"\n'{name}' updated successfully.")


# Delete a product
def delete_product():
    global df
    name = input("Enter product name: ")
    if name not in df.index:
        print("Product not found.")
        return

    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ")
    if confirm.lower() == 'y':
        df.drop([name], inplace=True)
        print(f"'{name}' removed from inventory.")
    else:
        print("Deletion cancelled.")


# Filter products by category
def filter_by_category():
    print("\nAvailable categories:")
    print(", ".join(df['Category'].unique()))

    category = input("\nEnter category to filter by: ")
    filtered = df[df['Category'] == category]

    if filtered.empty:
        print("No products found in that category.")
    else:
        print(f"\n{category} products:")
        print(filtered.to_string())


# Main program
print("Welcome to the Kinderland Inventory Manager!")

while True:
    print("\nOptions:"
          "\n 1. View full inventory"
          "\n 2. Search product"
          "\n 3. Add product"
          "\n 4. Update product (price / stock)"
          "\n 5. Delete product"
          "\n 6. Filter by category"
          "\n 7. Exit")

    try:
        option = int(input("\nSelect an option: "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if option == 1:
        view_inventory()
    elif option == 2:
        search_product()
    elif option == 3:
        add_product()
    elif option == 4:
        update_product()
    elif option == 5:
        delete_product()
    elif option == 6:
        filter_by_category()
    elif option == 7:
        print("Saving changes and exiting...")
        break
    else:
        print("Invalid option.")

df.to_csv('kinderland_inventory.csv', index_label='Product')
print("Inventory saved.")