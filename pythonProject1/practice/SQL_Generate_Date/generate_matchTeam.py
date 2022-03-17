import random
counter = 0
index_select =0
match_ID = 10, 3, 11, 5, 6, 19, 2, 13, 7, 17, 4, 20, 8, 14, 15, 16, 18, 1, 9, 12
team_ID = 17, 15, 20, 6, 5, 4, 9, 11, 12, 10, 18, 13, 7, 19, 14, 2, 3, 16, 1, 8
for x in range(20):
    counter +=1
    print("INSERT" + " INTO epl.MatchTeam VALUES(" + str(counter) + "," , str(match_ID[index_select])+ "," ,str(team_ID[index_select]) +");")
    index_select +=1