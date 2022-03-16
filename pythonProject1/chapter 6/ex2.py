def convert_euro(amount_euro, dollar_rate):
    return int(amount_euro) * float(dollar_rate)


dollar_rate = input("Current dollar rate (€ -> $): ")
amount_euro = input("Your amount in Euro: ")


print("€", amount_euro, "=", "$", convert_euro(amount_euro, dollar_rate))
