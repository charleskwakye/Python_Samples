import random
import names
counter = 0
index_select =0
team_ID = 7, 20, 10, 3, 1, 6, 17, 19, 14, 2, 8, 15, 16, 13, 12, 18, 11, 4, 9, 5
starting_eleven_ID = 2, 14, 20, 16, 3, 5, 17, 13, 18, 7, 11, 1, 6, 19, 9, 8, 12, 15, 4, 10
for x in range(20):
    position = "CF", "LW", "RW", "CAM", "CM", "DM", "CB", "RB", "LB", "GK"
    counter +=1
    print("INSERT" + " INTO epl.Player VALUES(" + str(counter) + "," , str(team_ID[index_select]) + "," , str(starting_eleven_ID[index_select])+", '" + names.get_full_name(gender='male')+"',", str(random.randint(19,36))+ ", '"+ position[random.randint(0,9)] + "',", str(random.randint(1,6))+",", str(random.randint(155,195))+");")
    index_select +=1