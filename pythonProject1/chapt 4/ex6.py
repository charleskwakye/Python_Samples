new_text =''
text = input('Enter a string?: ')
for i in range(0,len(text)-2,3):
    new_text = new_text + text[i+1]
    new_text = new_text + text[i+2]
    new_text = new_text + text[i]

new_text =new_text + text[i+3:]

print(new_text)

