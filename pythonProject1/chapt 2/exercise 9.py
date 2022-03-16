a = int(input("number 1 (0, 1 or 2): "))
b = int(input("number 1 (0, 1 or 2): "))
c = int(input("number 1 (0, 1 or 2): "))

if a == b and b == c:
    if a == 2:
        answer = 10
    else:
        answer = 5
else:
    if a != b and a != c:
        answer = 1
    else:
        answer = 0
print(answer)
