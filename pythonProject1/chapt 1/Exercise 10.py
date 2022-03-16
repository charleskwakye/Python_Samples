Fc = float(83.6)
Dp = int(input("Power consumption during the day(kilowatt per hour: "))
Np = int(input("Power consumption during the night(kilowatt per hour: "))


# Calculations
Dc = Dp * float(0.068)
Nc = Np * float(0.035)
TxV = Dc + Nc + Fc
TiV = Dc + Nc + ((TxV/100)*21)

print(str("Invoice" "\n***********" "\nFixed costs: € " + str(Fc)))
print(str("Daily Consumption: € " + str(Dc)))
print(str("Night consumption: € " + str(Nc)))
print(str("Total excluding VAT: € " + str(TxV)))
print(str("Total including VAT: € " + str(TiV)))
