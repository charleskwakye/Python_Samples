time = int(input("What time is it: "))
wait = int(input("How long do you want to wait: "))

tt = time + wait

while tt >= 49:
    tt = tt - 24
if tt >= 24:
    print(str((tt) - 24) + str(":00"))
elif tt < 24:
    print(str(tt) + str(":00"))
