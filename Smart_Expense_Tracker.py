import json
import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.json"

deleted_stack = []

# Load data
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {"budget": 0, "expenses": []}

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Set Monthly Budget
def set_budget(data):
    try:
        budget = float(input("Enter Monthly Budget: ₹"))
    except ValueError:
        print("Invalid budget.")
        return
    data["budget"] = budget
    save_data(data)
    print("Budget saved successfully.")

# Calculate Total Spending
def total_spent(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total

# Budget Alerts
def check_budget(data):
    budget = data["budget"]
    if budget == 0:
        return

    spent = total_spent(data["expenses"])
    percentage = (spent / budget) * 100
    print("\n===== Budget Monitor =====")
    print(f"Budget Used: {percentage:.1f}%")

    if percentage >= 100:
        print("\n⚠ BUDGET EXCEEDED!")
        print(f"You have exceeded your budget by ₹{spent-budget:.2f}.")
        print("Try postponing non-essential expenses until next month.")
    elif percentage >= 90:
        print("\n⚠ CRITICAL ALERT")
        print("You have almost exhausted your monthly budget.")
        print("Avoid unnecessary shopping and entertainment expenses.")
    elif percentage >= 75:
        print("\n⚠ WARNING")
        print("A significant portion of your budget has already been used.")
        print("Track your remaining expenses carefully.")
    elif percentage >= 50:
        print("\n📢 BUDGET NOTICE")
        print("Half of your monthly budget has been utilized.")
        print("Continue spending mindfully.")
    else:
        pass

# Add Expense
def add_expense(data):
    category = input("Enter Category: ")
    try:
        amount = float(input("Enter Amount: ₹"))
    except ValueError:
        print("Invalid amount.")
        return
    expense = {
        "date": str(datetime.date.today()),
        "category": category,
        "amount": amount
    }
    data["expenses"].append(expense)
    save_data(data)
    print("Expense Added Successfully.")
    check_budget(data)

# View Expenses
def view_expenses(data):
    expenses = data["expenses"]

    if not expenses:
        print("No Expenses Found.")
        return

    print("\n===================================")
    print("         EXPENSE RECORDS")
    print("===================================")
    print("No.\tDate\t\tCategory\tAmount")
    
    for i, exp in enumerate(expenses):
        print(
            f"{i+1}. "
            f"{exp['date']}\t"
            f"{exp['category']}\t"
            f"₹{exp['amount']}"
        )

# Search Expense
def search_expense(data):
    category = input("Enter Category: ").lower()
    found = False

    for exp in data["expenses"]:
        if exp["category"].lower() == category:
            print(
                f"{exp['date']} | "
                f"{exp['category']} | "
                f"₹{exp['amount']}"
            )
            found = True

    if not found:
        print("No Matching Expense Found.")

# Sort Expenses
def sort_expenses(data):
    if not data["expenses"]:
        print("No Expenses Found.")
        return
    print("1. Amount Ascending")
    print("2. Amount Descending")
    print("3. Date Ascending")
    print("4. Date Descending")
    choice = input("Enter Choice: ")

    if choice == "1":
        sorted_expenses = sorted(
            data["expenses"],
            key=lambda x: x["amount"]
        )
    elif choice == "2":
        sorted_expenses = sorted(
            data["expenses"],
            key=lambda x: x["amount"],
            reverse=True
        )
    elif choice == "3":
        sorted_expenses = sorted(
            data["expenses"],
            key=lambda x: x["date"]
        )
    elif choice == "4":
        sorted_expenses = sorted(
            data["expenses"],
            key=lambda x: x["date"],
            reverse=True
        )
    else:
        print("Invalid Choice")
        return
    print("\nSorted Expenses:\n")

    for exp in sorted_expenses:
        print(
            f"{exp['date']} | "
            f"{exp['category']} | "
            f"₹{exp['amount']}"
        )

# Delete Expense
def delete_expense(data):
    view_expenses(data)
    try:
        num = int(input("\nEnter Expense Number To Delete: "))
    except ValueError:
        print("Invalid Input")
        return

    if num < 1 or num > len(data["expenses"]):
        print("Invalid Choice")
        return

    deleted_stack.append(data["expenses"][num - 1])
    data["expenses"].pop(num - 1)
    save_data(data)
    print("Expense Deleted.")

# Undo Delete
def undo_delete(data):
    if not deleted_stack:
        print("Nothing To Undo.")
        return

    restored = deleted_stack.pop()
    data["expenses"].append(restored)
    save_data(data)
    print("Last Deleted Expense Restored.")

# Budget Status
def budget_status(data):
    budget = data["budget"]
    spent = total_spent(data["expenses"])
    expense_count = len(data["expenses"])
    remaining = budget - spent
    print("\n===================================")
    print("         BUDGET STATUS")
    print("===================================")
    print(f"Budget    : ₹{budget}")
    print(f"Spent     : ₹{spent}")
    print(f"Transactions : {expense_count}")
    print(f"Remaining : ₹{remaining}")

    if budget > 0:
        print(
            f"Usage     : "
            f"{(spent/budget)*100:.2f}%"
        )

# Expense Chart
def show_chart(data):

    if not data["expenses"]:
        print("No Data Available.")
        return

    category_totals = {}

    for exp in data["expenses"]:
        category = exp["category"]
        category_totals[category] = (
            category_totals.get(category, 0)
            + exp["amount"]
        )
    plt.pie(
        category_totals.values(),
        labels=category_totals.keys(),
        autopct="%1.1f%%"
    )
    plt.title("Expense Distribution")
    plt.show()

# Main Program
def main():
    data = load_data()
    while True:
        print("\n===================================")
        print("     SMART EXPENSE TRACKER")
        print("===================================")
        print("\n1. Set Monthly Budget")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Search Expense")
        print("5. Sort Expenses")
        print("6. Delete Expense")
        print("7. Undo Delete")
        print("8. Budget Status")
        print("9. Expense Chart")
        print("10. Exit")
        print("-----------------------------------")

        choice = input("Enter Choice: ")
        if choice == "1":
            set_budget(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            view_expenses(data)
        elif choice == "4":
            search_expense(data)
        elif choice == "5":
            sort_expenses(data)
        elif choice == "6":
            delete_expense(data)
        elif choice == "7":
            undo_delete(data)
        elif choice == "8":
            budget_status(data)
        elif choice == "9":
            show_chart(data)
        elif choice == "10":
            print("Thank You!")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
