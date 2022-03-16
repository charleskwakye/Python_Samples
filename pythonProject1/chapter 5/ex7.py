numbers = [2, 5, 7, 9]
length = len(numbers) * 2
zeros = [0]*(length)
zeros = zeros[:-1]
zeros.append(numbers[-1])
print(zeros)