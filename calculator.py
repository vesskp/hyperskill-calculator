# Define the earnings for each item
earnings = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}

# Print the earned amount for each item
print("Earned amount:")
for item, amount in earnings.items():
    print(f"{item}: ${amount}")

# Calculate the total income
total_income = sum(earnings.values())
print(f"\nIncome: ${total_income}")

# Ask the user for staff expenses
staff_expenses = int(input("Staff expenses: "))

# Ask the user for other expenses
other_expenses = int(input("Other expenses: "))

# Calculate the net income
net_income = total_income - staff_expenses - other_expenses

# Print the net income
print(f"Net income: ${net_income}")
