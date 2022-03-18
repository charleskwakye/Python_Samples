import random


index_s = 0
counter = 0

match_id = 18, 19, 14, 1, 15, 7, 17, 6, 10, 12, 8, 4, 5, 20, 3, 2, 11, 9, 16, 13
eleven_id = 9, 20, 12, 4, 16, 13, 11, 17, 5, 15, 18, 3, 19, 10, 7, 8, 6, 1, 14, 2

for x in range(20):
    counter += 1
    per_m_id = str(match_id[index_s])
    per_e_id = str(eleven_id[index_s])
    print("INSERT" + " INTO epl.MatchStartingEleven VALUES(" + str(counter) + "," ,"'" + per_m_id+"'" + "," ,"'" + per_e_id+"'" +");")
    index_s +=1
