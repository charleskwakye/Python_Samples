rate = float(input("Enter the current exchange dollar rate (€ -> $): "))
amount = int(input("Enter your amount in euro: "))

# Calculations
converted = amount * rate
print(str(amount) + " €" + " = ", converted, " $")
