# Smart Expense Tracker with Budget Monitoring

## Overview

Smart Expense Tracker is a Python-based command-line application that helps users record, organize, and monitor their daily expenses. The application stores expense records in JSON format, tracks spending against a monthly budget, and generates alerts when predefined budget utilization thresholds are reached.
The project was developed to strengthen concepts such as Python programming, file handling, data structures, searching and sorting, and data visualization.

---

## Features

### Expense Management

* Add new expenses with category and amount
* View all recorded expenses
* Delete existing expenses
* Restore the last deleted expense using Undo functionality
* Search expenses by category
* Sort expenses by amount or date

### Budget Monitoring

* Set a monthly budget
* Track total spending
* View remaining budget
* Monitor budget utilization percentage
* Receive alerts when spending reaches:

  * 50% of budget
  * 75% of budget
  * 90% of budget
  * Budget exceeded

### Data Visualization

* Generate category-wise expense distribution using a Pie Chart
* Visualize spending patterns through graphical representation

### Data Persistence

* Store expense records in JSON format
* Automatically load previously saved records on startup

---

## Technologies Used

* Python
* JSON
* Matplotlib
* File Handling
* Data Structures

---

## Data Structures and Concepts Used

| Feature              | Concept Used          |
| -------------------- | --------------------- |
| Expense Storage      | List                  |
| Expense Records      | Dictionary            |
| Undo Delete          | Stack                 |
| Category Aggregation | Hash Map (Dictionary) |
| Expense Search       | Linear Search         |
| Expense Sorting      | Sorting               |
| File Storage         | JSON File Handling    |

---

## Project Structure

```text
SmartExpenseTracker/
│
├── Smart_Expense_Tracker.py
├── expenses.json
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── main_menu.png
    ├── expense_records.png
    ├── budget_status.png
    └── pie_chart.png
    └── budget_alert.png
```

---

## Installation and Usage

### Clone Repository

```bash
git clone <repository-url>
cd SmartExpenseTracker
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python Smart_Expense_Tracker.py
```

Note: The above commands work in both Command Prompt and PowerShell. If Python is not recognized in PowerShell, you may need to use:

```bash
python3 Smart_Expense_Tracker.py
```

or ensure Python is added to your system PATH.

---

## How the System Works

1. The user sets a monthly budget.
2. Expenses are recorded with date, category, and amount.
3. Data is stored persistently in a JSON file.
4. The system calculates total spending and remaining budget.
5. Budget utilization is monitored whenever a new expense is added.
6. Alerts are displayed when spending crosses predefined budget thresholds.
7. Users can search, sort, delete, and restore expense records.
8. Expense distribution can be visualized using a pie chart.

---

## Learning Outcomes

Through this project, the following concepts were explored:

* Python Programming Fundamentals
* File Handling
* JSON Data Storage
* Data Structures
* Searching and Sorting
* Exception Handling
* Data Visualization using Matplotlib
* Budget Tracking Logic

---

## Future Enhancements

* Monthly expense summary reports
* Category-wise spending limits
* Budget forecasting based on spending trends
* SQLite database integration
* Graphical User Interface (GUI)
* Export expense reports to CSV

---

## Author

**Krishvika**
