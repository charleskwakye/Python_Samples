list = (1, 2, 3, 4, 5, 4, 6, 7, 8, 9)
print(list)
is_found = False
index = len(list)
while not is_found and index>0:
    index -= 1
    if list[index] == 4:
        is_found = True
if not is_found:
    print("The number 4 does not in the Tuple")
else:
    print(list[index+1:])