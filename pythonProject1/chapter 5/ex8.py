scores = []
print('Enter the scores for the test. Use _1 if you want to finish')
score = float(input("Score:"))

while score != -1:
    scores.append(score)
    score = float(input("Score: "))

if len(scores) > 0:
    scores.sort()
    print('The score (ordered): ', scores)
    print('The average of these', len(scores), 'scores =', sum(scores)/len(scores))
