# def stringCounter(txt):
#     upper = 0
#     lower = 0
#     for i in range(len(txt)):
#         if txt[i] >='a' and txt[i]<='z':
#             lower+=1
#
#         elif txt[i]>='A' and txt[i]<='Z':
#             upper+=1
#
#     print('Number of lower case letters:', lower)
#     print('Number of lower Capitals:', upper)
#
# text = input('Your string: ')
# stringCounter(text)
def checker(text):
    result = []
    iscapital = issmall = 0
    for letter in text:
        if letter.isupper():
            iscapital = iscapital + 1
        elif letter.islower():
            issmall = issmall + 1
    result.append(iscapital)
    result.append(issmall)
    return result

pas = input("Set your password(at least 2 uppercase and 3 lowercase letters): ")
reply = checker(pas)
feedback = False
while feedback is False:
    if reply[0] >=2 and reply[1]>=3:
        print('Password Valid')
        feedback = True
    else:
        pas = input("Set your password(at least 2 uppercase and 3 lowercase letters): ")
        reply = checker(pas)
