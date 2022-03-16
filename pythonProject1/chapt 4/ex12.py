text = input("Enter a string: ")
position_star = text.find('*')
while position_star != -1:
    text = text[0:position_star-1] + text[position_star+2:]
    position_star = text.find('*')
print(text)
