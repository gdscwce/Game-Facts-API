import json, random
from os import listdir

def open_file(game):
    with open(f'data/{game}.json', 'r') as file:
        data = json.load(file, strict=False)
    return [data, len(data)]
def random_file():
    file = random.choice(listdir("data/"))
    with open("data/"+file) as random_file:
        data = json.load(random_file, strict=False)
    return [data,len(data),file]