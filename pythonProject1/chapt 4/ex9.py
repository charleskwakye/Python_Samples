food = input("What do you eat for lunch: ")
first = food.find("sandwich")
if first != 1:
    second_part = food[first+8:]
    second_position = second_part.find("sandwich")
    if second_position != -1:
        print("you have", second_part[0:second_position], "between your sandwich")
