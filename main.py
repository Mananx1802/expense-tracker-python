expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Expense Name: ")
        amount = float(input("Amount: ₹"))
        expenses.append((name, amount))
        print("Expense Added Successfully!")

    elif choice == "2":
        total = 0

        if not expenses:
            print("No expenses found.")

        for name, amount in expenses:
            print(f"{name}: ₹{amount}")
            total += amount

        print(f"\nTotal Spending: ₹{total}")

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice!")
