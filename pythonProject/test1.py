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

string = 'Life of Brian'
print(counter_f(string))