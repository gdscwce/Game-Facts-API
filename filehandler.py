import json

def open_file(game):
    with open(f'data/{game}.json', 'r') as file:
        data = json.load(file, strict=False)
    return [data, len(data)]