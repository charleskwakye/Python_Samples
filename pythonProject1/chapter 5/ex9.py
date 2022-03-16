names = []
distances = []
print('Enter your name and the distance to school')
print('Type stop when you want to close the entry')
# step 1 reading
name = input('Your name: ')
while name != 'stop':  # step 2 checking with while
    # step 3 doing sth
    distance = float(input('Your distance: '))
    names.append(name)
    distances.append(distance)
    name = input('Your names? ')  # step 4 reading again
# print(names,distances)
if len(names) != 0:
    print('Overview')
    for i in range(len(names)):
        print(names[i],'\t', distances[i])
    max_km = max(distances)
    print(names[distances.index(max_km)], 'lives farthest, namely', max_km, 'km')
    print('The average distance is', sum(distances)/len(distances))

