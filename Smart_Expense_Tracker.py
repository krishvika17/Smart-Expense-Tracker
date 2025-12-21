def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (DD-MM-YYYY): ")
    note = input("Note: ")

    expense = {
        "Amount": amount,
        "Category": category,
        "Date": date,
        "Note": note
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded!")
        return

    for exp in expenses:
        print(exp)

def total_expenditure(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]
    print("Total spending:", total)

def category_summary(expenses):
    summary = {}

    for exp in expenses:
        category = exp["category"]

        if category not in summary:
            summary[category] = 0

        summary[category] += exp["amount"]

    for category, amount in summary.items():
        print(category, ":", amount)

def highest_spending_category(expenses):
    summary={}
    for exp in expenses:
        category = exp["category"]

        if category not in summary:
            summary[category] = 0

        summary[category] += exp["amount"]

    highest_amount = max(summary.values())
    for category, amount in summary.items():
        if amount == highest_amount:
            highest_category = category
            break

    print(highest_category, ":", highest_amount)


import json

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def main():
    expenses = load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenditure")
        print("4. Category Summary")
        print("5. Highest Spending Category and amount")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenditure(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            highest_spending_category(expenses)
        elif choice == "6":
            save_expenses(expenses)
            break
        else:
            print("Invalid choice")
