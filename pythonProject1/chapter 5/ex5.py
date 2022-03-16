numbers = [0, 42, 18, 17, 0, 2, 19, 10, 5, 14]
for i in range(len(numbers)-1):
    if numbers[i] == 0:
        largest_odd = 0
        for j in range(i+1, len(numbers)):
            if numbers[j] % 2 != 0 and numbers[j] > largest_odd:
                largest_odd = numbers[j]
        numbers[i] = largest_odd
print(numbers)
