import json #to store data in a file
import datetime #to get current date
import matplotlib.pyplot as plt #visual representation of data

FILE_NAME = "expenses.json" 


# Load expenses from JSON file
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


# Save expenses to JSON file
def save_expenses(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Add new expense
def add_expense(expenses):
    category = input("Enter category (food/travel/shopping/etc): ")
    amount = float(input("Enter amount: "))
    date = str(datetime.date.today())

    expense = {
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense) #add expense dict to a list 
    save_expenses(expenses)

    print("Expense added successfully!")


# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nDate\t\tCategory\tAmount")

    for exp in expenses:
        print(f"{exp['date']}\t{exp['category']}\t\t₹{exp['amount']}")


# Monthly report
def monthly_report(expenses):
    month = datetime.date.today().month
    total = 0

    for exp in expenses:
        exp_month = int(exp["date"].split("-")[1])
        if exp_month == month:
            total += exp["amount"]

    print(f"\nTotal spending this month: ₹{total}")


# Budget check
def budget_alert(expenses):
    limit = float(input("Enter your monthly budget: "))
    total = 0

    for exp in expenses:
        total = total + exp["amount"]

    if total > limit:
        print("⚠️ Budget exceeded!")
    else:
        print("You are within budget.")


# Expense pie chart
def show_chart(expenses):
    if not expenses:
        print("No data to display.")
        return

    category_totals = {}

    for exp in expenses:
        category = exp["category"]
        category_totals[category] = category_totals.get(category, 0) + exp["amount"]#NEW DICT FOR CATEGORY TYPE AND VALUE STORAGE

    labels = category_totals.keys()
    values = category_totals.values()

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()


# Main program
def main():
    expenses = load_expenses()

    while True:
        print("\nSMART EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Report")
        print("4. Budget Check")
        print("5. Expense Chart")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            monthly_report(expenses)

        elif choice == "4":
            budget_alert(expenses)

        elif choice == "5":
            show_chart(expenses)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
