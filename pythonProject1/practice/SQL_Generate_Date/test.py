import random

tournament = "Champions League", "EPL", "La Liga", "Seria A", "Bundesliga A", "Carabao Cup", "Europa League","Club World cup"
organisation = "UEFA","The Premier League","Spanish FA","Italian FA","German FA","English FA","UEFA","FIFA"
per_tournament = tournament[random.randint(0,len(tournament) -1)]
per_organisation = organisation[tournament.index(per_tournament)]

print(per_tournament)
print(per_organisation)
#print(organisation[tournament.index(per_tournament)])