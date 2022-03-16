date_of_birth = int(input('Enter your year of birth: '))
calculations = 2021 - date_of_birth
print("Your age =",calculations)
if calculations >= 18:
    print("You're an adult")
else:
    print("You're not an adult yet.")