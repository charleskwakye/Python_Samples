import random

counter = 0
select_index = 0
referee ="Valeriano Holme","Mort Moors","Bevis Jiménez","Odoacre Bakhuizen","Jadyn Lowry","Broos Wheeler",\
         "Willard Sims","Enzo Gil","Severo Freudenberger","Angelino Pearson","Rodolf Schuchert","Gottlob Baggio",\
         "Dom Presley","Clifford Biondi","Augustine Saunders","Rodolf Schuchert","Gottlob Baggio","Dom Presley",\
         "Clifford Biondi","Augustine Saunders"
tournament_ID = 15, 16, 7, 8, 13, 3, 2, 6, 12, 11, 1, 20, 4, 19, 17, 9, 5, 10, 18, 14
year = "2020","2021", "2022"
stadium = "Villa Park","The Amex","Turf Moor","Elland Road","King Power Stadium","Goodison Park","Anfield",\
          "Emirates Stadium","Brentford Community Stadium","Stamford Bridge","Selhurst Park",\
          "Tottenham Hotspur Stadium","London Stadium","Etihad Stadium","Old Trafford","St James Park","Carrow Road",\
          "St Marys Stadium","Vicarage Road","Molineux Stadium"
opponent= "Aston Villa","Brighton & Hove Albion","Burnley","Leeds United","Leicester City","Everton","Liverpool",\
               "Arsenal","Brentford","Chelsea","Crystal Palace","Tottenham Hotspur","WestHam United","Manchester City",\
               "Manchester United","Newcastle United","Norwich City","Southampton","Watford","Wolverhampton Wanderers"
for x in range(20):
    counter +=1
    referee_name = str(referee[select_index])
    match_date = "'" +str(random.randint(2020,2022))+"-"+str(random.randint(1,12))+"-"+str(random.randint(1,30))+"'"
    yellow_cards = str(random.randint(0,6))
    red_cards = str(random.randint(0,2))
    stadium_name= str(stadium[select_index])
    opponent_name = str(opponent[select_index])
    result = str(random.randint(0,5))+"-"+str(random.randint(0,5))
    print("INSERT" + " INTO epl.Match VALUES(" + str(counter) + ",", str(tournament_ID[select_index]) + ",", "'"+referee_name+"'"+"," ,match_date+",", "'"+yellow_cards +"'"+ "," , "'"+red_cards+"'" + "," ,"'"+result+"'"+",", "'"+stadium_name+"'"+"," ,"'" + opponent_name+"'"+");")
    select_index +=1