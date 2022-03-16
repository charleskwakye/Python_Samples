# Ex5
def counter_f(string):
    info = []
    raw_string = []
    capital = 0
    small = 0
    for letter in string:
        if letter != ' ':
            raw_string.append(letter)
    for i in raw_string:
        if i.isupper():
            capital = capital + 1
        else:
            small = small + 1
    info.append(capital)
    info.append(small)
    return info

string = input('Set your password (at least 2 uppercase and 3 lowercase letters): ')

while counter_f(string)[0] <= 2 or counter_f(string)[1] <=3:
        string = input('Set your password (at least 2 uppercase and 3 lowercase letters): ')