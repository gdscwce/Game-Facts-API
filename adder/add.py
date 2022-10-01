# Converts facts from a text file to a json, puts it inside the correct directory and adds new endpoint to the main API automatically

import json
name = str(input("Input the name of the game without spaces: "))
facts = []
with open('adder/facts.txt', "r") as text:
    for index,line in enumerate(text.readlines(),1):
        facts.append(dict(id = index,fact = line.strip()))
        
with open(f"game-facts/data/{name}.json", "a") as finalfile:
    finalfile.write(json.dumps(facts,sort_keys=False, indent=4))

with open("game-facts/main.py", "a") as pyfile:
    pyfile.write(f"""@app.get("/{name}/")
async def read_item(limit: int = -1, random: bool = False):
    with open('{name}.json', "r", encoding='utf-8') as json_file:
        allFacts = json.load(json_file, strict=False)
    countAllFacts = len(allFacts)
    if limit < 0 or limit >= countAllFacts:
        if random == False:
            return allFacts
        Rand.shuffle(allFacts)
        return allFacts
    if limit == 0:
        return []
    if random:
        Rand.shuffle(allFacts)
        requiredFacts = []
        for i in range(limit):
            requiredFacts.append(allFacts[i])
        return requiredFacts
    requiredFacts = []
    for i in range(limit):
        requiredFacts.append(allFacts[i])
    return requiredFacts""")



