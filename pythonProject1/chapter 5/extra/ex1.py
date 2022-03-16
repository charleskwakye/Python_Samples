digits=[]
letters=[]
# isdigit() islower() isupper()
text= input('Pass your string of characters ')
for item in text:
    if item.isdigit():
        digits.append(item) # add at the end
    elif item.islower():
        letters.insert(0,item) #add at the begin
    elif item.isupper():
        letters.append(item)
print(digits+letters)