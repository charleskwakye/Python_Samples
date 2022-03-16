current_time = int(input("Enter the current hour:"))
wait_time = int(input("How long do you want to wait: "))

end_time = current_time + wait_time
alarm_time = end_time % 24

print("The alarm will sound at"+str(alarm_time)+'h.')
