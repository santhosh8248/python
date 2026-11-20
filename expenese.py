
class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    def add_expense(self):
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        self.expenses.append({
            "name": name,
            "amount": amount
        })

        print("Expense added!")

    def view_expenses(self):
        for expense in self.expenses:
            print(expense["name"], expense["amount"])

    def total_expenses(self):
        total = 0

        for expense in self.expenses:
            total += expense["amount"]

        print("Total Expense:", total)


obj = ExpenseTracker()

while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        obj.add_expense()

    elif choice == "2":
        obj.view_expenses()

    elif choice == "3":
        obj.total_expenses()

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
