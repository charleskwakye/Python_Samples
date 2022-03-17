import random
counter = 0
index_select = 0
for x in range(20):
    tournament = "Champions League", "EPL", "La Liga", "Seria A", "Bundesliga A", "Carabao Cup", "Europa League", "Club World cup"
    organisation = "UEFA", "The Premier League", "Spanish FA", "Italian FA", "German FA", "English FA", "UEFA", "FIFA"
    per_tournament = tournament[random.randint(0, len(tournament) - 1)]
    per_organisation = organisation[tournament.index(per_tournament)]
    counter +=1
    print("INSERT" + " INTO epl.Tournament VALUES(" + str(counter) + "," ,"'" + per_tournament+"'" + "," ,"'" +per_organisation+"'" +");")
    index_select +=1