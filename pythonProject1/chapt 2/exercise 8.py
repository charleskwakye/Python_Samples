# check if party is good 5 bottles, 5 wine
# check if it is, fantastic double bottles or double of wine
# else stupid
wine = int(input("How many bottles of wine are there: "))
pizza = int(input('How many pizzas are there: '))

if wine and pizza >= 5:
    if wine // 2 >= pizza or pizza // 2 >= wine:  # check the second the argument before printing anything
        print("This is a fantastic party")  # print this if it is true
    else:
        print("This is a good party")  #  if second argument not true print this statement. This prints because you are still in loop
else:
    print("This is just a stupid party")
