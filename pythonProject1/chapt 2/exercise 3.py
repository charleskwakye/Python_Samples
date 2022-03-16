number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
number_3 = int(input("Number 3: "))

smallest = number_1
if number_2 < smallest:
    smallest = number_2
if number_3 < smallest:
    smallest = number_3

print("The smallest number is", smallest)
