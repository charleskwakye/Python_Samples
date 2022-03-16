def lowest_price():
    name_lowest_dictionary = {}
    with open('Files Chapter 12/prices.txt') as file:
        line = file.readline()
        while line:
            record = line.rstrip().split(';')
            name = record[0]
            price = record[1]
            while line and record[0] == name:
                if record[1] < price:
                    price = record[1]
                else:
                    line = file.readline()
                    record = line.rstrip().split(';')
            name_lowest_dictionary[name] = price  # making dictionary
    return name_lowest_dictionary


# main program
name_lowest_dictionary = lowest_price()

print('Price list')
print('-'* len('Price list'))
for data in name_lowest_dictionary:   # Printing data beside each element in the dictionary
    print(data,'\t'+ name_lowest_dictionary[data])

user_input = input('Enter the item(press x if you want to stop:')
while user_input.upper() != 'X':
    if user_input not in name_lowest_dictionary:
        print('This item is not available.')
    else:
        print('The lowest price of', user_input,'is', name_lowest_dictionary.get(user_input))
        user_input = input('Enter the item(press x if you want to stop:')

