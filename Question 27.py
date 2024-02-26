def calculate_tax(income):
    if income <= 150000:
        return 0
    elif 150001 <= income <= 300000:
        return 0.1 * (income - 150000)
    elif 300001 <= income <= 500000:
        return 0.2 * (income - 300000) + 15000  # 10% on first 150,000 and 20% on the remaining
    else:
        return 0.3 * (income - 500000) + 45000  # 10% on first 150,000, 20% on next 200,000, and 30% on the rest

# Example usage:
income = int(input("Enter your income: "))
tax = calculate_tax(income)
print(f"Tax to be paid: {tax}")

