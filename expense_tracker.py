import os

EXPENSES_FILE = "expenses.txt"

def add_expense(date, amount, category, description):
    with open(EXPENSES_FILE, "a") as f:
        f.write(f"{date},{amount},{category},{description}\n")
    print("Expense added!")

def view_expenses():
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return
    with open(EXPENSES_FILE, "r") as f:
        print("Date       | Amount  | Category   | Description")
        print("-----------------------------------------------")
        for line in f:
            date, amount, category, description = line.strip().split(",", 3)
            print(f"{date:10} | {amount:7} | {category:10} | {description}")

def summary_by_category():
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return
    summary = {}
    with open(EXPENSES_FILE, "r") as f:
        for line in f:
            _, amount, category, _ = line.strip().split(",", 3)
            summary[category] = summary.get(category, 0) + float(amount)
    print("Category-wise Expense Summary:")
    for cat, total in summary.items():
        print(f"{cat}: {total:.2f}")

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Summary by category")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            add_expense(date, amount, category, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()