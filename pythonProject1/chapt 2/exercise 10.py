# check three numbers
# print both are ok if numbers is between 30 and 40 (inclusive)
# print both are ok if they are 65,72,82 and 90

first_number = int(input("First number: "))
second_number = int(input("Second number: "))

if first_number in range(30, 41) and second_number in range(30,41) or first_number in [65, 72, 83, 90] and second_number in [65, 72, 83, 90]:
    print('Both numbers are ok')
else:
    print('They are not ok')