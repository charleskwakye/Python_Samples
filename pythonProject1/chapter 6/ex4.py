import random
def generate_list(number,lower,upper):
    random_list = []
    for i in range(number):
        random_list.append(random.randint(lower,upper))  #upper is included
    return random_list


def filter_list(list):
    list_unique_value=[]
    for item in list:
        if item not in list_unique_value:
            list_unique_value.append(item)
    return list_unique_value


# result_list = generate_list(10,15,35)
# print(result_list)
# print(filter_list(result_list))
# number = int(input("How many dice do you want to roll: "))
# list_random_values = generate_list(number,1,6)
# print("You threw: ",list_random_values)
# print("Your unique rolls were: ",filter_list(list_random_values))

list_random_values = generate_list(5,1,6)
print(list_random_values)
counter=0
while len(filter_list(list_random_values)) != 1:
    print("You threw: ",list_random_values)
    counter+=1
    list_random_values=generate_list(5,1,6)
    print("You threw: ",list_random_values)
    print('You threw poker after',counter,'time.')