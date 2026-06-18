import matplotlib.pyplot as plt
import csv
import os

# File name for storing data
FILE_NAME = "expenses.csv"

def add_expense():
    category = input("Enter the expense category (e.g., Food, Travel, Shopping): ")
    try:
        amount = int(input("Enter the amount: "))
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])
        print("Expense saved successfully! ✅\n")
    except ValueError:
        print("Please enter only numbers for the amount! ❌\n")

def show_chart():
    if not os.path.exists(FILE_NAME):
        print("No data available yet.")
        return

    categories = []
    amounts = []
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row: # Check for empty rows
                categories.append(row[0])
                amounts.append(int(row[1]))
    
    if amounts:
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title('My Expense Details')
        plt.show()
    else:
        print("Data is empty.")

# Menu Loop
while True:
    print("1. Add Expense")
    print("2. Show Chart")
    print("3. Exit")
    choice = input("Select an option (1/2/3): ")
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        show_chart()
    elif choice == '3':
        break
    else:
        print("Invalid option! Please try again.")
