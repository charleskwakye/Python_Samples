number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
number_3 = int(input("Number 3: "))

if number_1 + number_2 == number_3 or number_2 + number_3 == number_1 or number_1 + number_3 == number_2:
    print("This works")
else:
    print("This won't work")
