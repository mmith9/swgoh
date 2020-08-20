import json
import csv

from api_swgoh_help import api_swgoh_help, settings

# Change the settings below
creds = settings('smith007', '900FYO5683FJK2W6DFUYK57890')
client = api_swgoh_help(creds)

allycodes=[648777188]

print(allycodes)


# Fetch player information (one or more allycodes in a list)
project={}
#project['id']=1
#project['arena']=1
#project['name']=1

players = client.fetchPlayers(allycodes,project)

filename="test.json"
with open(filename,"w") as f:
    json.dump(players,f,indent=4)

print("name\tsquad rank\tship rank")

positions=["" for x in range(0,50)]

for player in players:
    name=player['name']
    squad_rank=player['arena']['char']['rank']
    ship_rank=player['arena']['ship']['rank']
    padding=""
    for i in range(0,25-len(name)):
        padding+=" "
    
    print(f"{name}{padding}{squad_rank}\t{ship_rank}")

    if squad_rank < 50:
        positions[squad_rank]=name

print(f"requested codes: {len(allycodes)}")
print(f"retrieved players: {len(players)}")

for x in range(1,50):
    print(f"{x}\t{positions[x]}")




