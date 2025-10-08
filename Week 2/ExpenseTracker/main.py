from core import add_expense, total_expenses, list_expenses
from storage import load_expenses, save_expenses

def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    expenses = load_expenses()

    while True:
        print("\n1) Add expense\n2) View expenses\n3) View total\n4) Save & Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            item = input("Item: ").strip().title()
            amount = read_float("Amount: ")
            try:
                add_expense(expenses, item, amount)
                print("Added.")
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            print("\nExpenses:")
            print(list_expenses(expenses))

        elif choice == "3":
            print(f"Total: {total_expenses(expenses):.2f}")

        elif choice == "4":
            save_expenses(expenses)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
