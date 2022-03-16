with open('Files Chapter 7/first_names.txt') as file:
    first_names = file.readlines()
    for i in range(len(first_names)):
        if i%10 == 0 and i!=0:
            print()
        print(first_names[i].rstrip().ljust(13), end='')
