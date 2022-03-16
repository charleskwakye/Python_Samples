text = input("Enter a text: ")
letters = []
for i in range(len(text)):
    if text[i] != ' ':
        letters.append(text[i])
print(text)
print(*letters)
print(*letters, sep='\t')
