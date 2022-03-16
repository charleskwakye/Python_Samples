numbers = [9, 17, 25, 4, 7, 12]
new_list = []
for number in numbers:
    if number % 2 == 0:
        new_list.insert(0, number)
    else:
        new_list.append(number)
print(numbers, 'becomes', new_list)
