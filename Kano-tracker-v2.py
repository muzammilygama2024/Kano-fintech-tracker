# Day 1: Kano Small Business Expense Tracker
# Software Engineering project - Nanjing

print("Welcome to Kano Business Tracker!")

# Ask for business name
business_name = input("Enter business name: ")

# Today's sales
sales = float(input("Enter today's sales: "))
expenses = float(input("Enter today's expenses: "))

# Calculate profit
profit = sales - expenses

print("\n--- RESULT ---")
print(f"Business: {business_name}")
print(f"Sales: N{sales}")
print(f"Expenses: N{expenses}")
if profit >= 0:
    print(f"Profit: N{profit} - Alhamdulillah!")
else:
    print(f"Loss: N{profit} - Tomorrow will be better")

# Save to file
with open("business_record.csv", "a") as f:
    f.write(f"{business_name},{sales},{expenses},{profit}\n")

print("Saved to business_record.csv")
