import json
import csv
import datetime

from api_swgoh_help import api_swgoh_help, settings

# Change the settings below
creds = settings('smith007', '900FYO5683FJK2W6DFUYK57890')
client = api_swgoh_help(creds)

filename="allycodes.csv"
with open(filename) as f:
    reader=csv.reader(f)
    allycodes=[]
    for ally in reader:
        try:
            print(ally)
            allycodes.append(ally[0])
        except:
            pass

print(allycodes)


# Fetch player information (one or more allycodes in a list)
project={}
#project['id']=1
project['arena']={"char":{"rank":3},"ship":{"rank":2}}
project['name']=2
project['updated']=2


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
    updated=int(player['updated'])
    updated=datetime.datetime.fromtimestamp(updated/1000)
    padding=""
    for i in range(0,25-len(name)):
        padding+=" "
    
    print(f"{name}{padding}{squad_rank}\t{ship_rank}\t{updated}")

    if squad_rank < 50:
        positions[squad_rank]=name

print(f"requested codes: {len(allycodes)}")
print(f"retrieved players: {len(players)}")

for x in range(1,50):
    print(f"{x}\t{positions[x]}")




