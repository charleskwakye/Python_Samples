##numbers = (1, 2, 3, 4, 5, 6, 7, 8)
numbers = (4, 5, 4, 6, 7, 8)
place_of_4 = numbers.index(4)
if 4 in numbers:
    print(numbers[place_of_4 + 1:])
