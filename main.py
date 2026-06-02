import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

expenses = load_expenses()

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Expense Name: ")
        amount = float(input("Amount: ₹"))

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense Added Successfully!")

    elif choice == "2":
        total = 0

        if not expenses:
            print("No expenses found.")

        for expense in expenses:
            print(f"{expense['name']}: ₹{expense['amount']}")
            total += expense["amount"]

        print(f"\nTotal Spending: ₹{total}")

    elif choice == "3":
        print("Data Saved Successfully!")
        break

    else:
        print("Invalid Choice!")
