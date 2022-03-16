initial_limit = int(input('Initial limit: '))
final_limit = int(input('Final limit: '))
if initial_limit > final_limit:
    print('The initial limit limit must be smaller than the final limit!')
else:
    sum = initial_limit
    print('Sum of numbers from', initial_limit, 'till', final_limit)
    if initial_limit == final_limit:
        print(sum)
    else:
        for i in range(initial_limit + 1, final_limit + 1):
            sum += 1
            print('+', i, '-->', sum)
            