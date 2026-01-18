# Initialize lists for item codes, prices, and quantities
codes = []
prices = []
quantities = []

# Input code and price for 5 items
print("Enter the code and price for 5 items:")
for i in range(5):
    code = input(f"Enter code for item {i + 1}: ")
    price = float(input(f"Enter price for item {i + 1}: "))
    codes.append(code)
    prices.append(price)

# Input quantity for each item
print("\nEnter quantity for each item:")
for i in range(5):
    quantity = int(input(f"Enter quantity for item '{codes[i]}': "))
    quantities.append(quantity)

# Display the billing details
print("\nBilling Details:")
print(f"{'Item Code':<15}{'Price':<10}{'Quantity':<10}{'Total Amount':<15}")
grand_total = 0
for i in range(5):
    total_amount = prices[i] * quantities[i]
    grand_total += total_amount
    print(f"{codes[i]:<15}{prices[i]:<10.2f}{quantities[i]:<10}{total_amount:<15.2f}")

# Display the grand total
print(f"\nGrand Total: {grand_total:.2f}")

