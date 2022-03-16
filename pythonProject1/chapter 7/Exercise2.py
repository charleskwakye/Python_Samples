with open("Files Chapter 7/first_names.txt") as file:
    first_names = file.readlines()
    first_names.reverse()
    #print(*first_names)
    for item in first_names:
        print(item, end=' ')
        