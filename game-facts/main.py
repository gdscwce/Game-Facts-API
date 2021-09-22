from fastapi import FastAPI
from deta import Deta
import json
import random as Rand
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
a = "c00viw7z_4Rj2TKrz3WGG3"
deta = Deta(a+"xWuLkW711vRCifgJ4GR")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Let's begin!"}


# Minecraft
@app.get("/minecraft/")
async def read_item(limit: int = -1, random: bool = False):
    with open('minecraft.json', "r", encoding='utf-8') as json_file:
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
    return requiredFacts

# GTA 5
@app.get("/gta5/")
async def read_item(limit: int = -1, random: bool = False):
    with open('gta5.json', "r", encoding='utf-8') as json_file:
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
    return requiredFacts

# # DOTA 2
# @app.get("/dota2/")
# async def read_item(limit: int = -1, random: bool = False):
#     with open('dota2.json', "r", encoding='utf-8') as json_file:
#         allFacts = json.load(json_file, strict=False)
#     countAllFacts = len(allFacts)
#     if limit < 0 or limit >= countAllFacts:
#         if random == False:
#             return allFacts
#         Rand.shuffle(allFacts)
#         return allFacts
#     if limit == 0:
#         return []
#     if random:
#         Rand.shuffle(allFacts)
#         requiredFacts = []
#         for i in range(limit):
#             requiredFacts.append(allFacts[i])
#         return requiredFacts
#     requiredFacts = []
#     for i in range(limit):
#         requiredFacts.append(allFacts[i])
#     return requiredFacts

# Farcry 5
@app.get("/farcry5/")
async def read_item(limit: int = -1, random: bool = False):
    with open('farcry5.json', "r", encoding='utf-8') as json_file:
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
    return requiredFacts

# CSGO
@app.get("/csgo/")
async def read_item(limit: int = -1, random: bool = False):
    with open('csgo.json', "r", encoding='utf-8') as json_file:
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
    return requiredFacts

# Siege
@app.get("/rainbowsiege6/")
async def read_item(limit: int = -1, random: bool = False):
    with open('siege.json', "r", encoding='utf-8') as json_file:
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
    return requiredFacts

# # The Witcher 3
# @app.get("/thewitcher3/")
# async def read_item(limit: int = -1, random: bool = False):
#     with open('theWitcher3.json', "r", encoding='utf-8') as json_file:
#         allFacts = json.load(json_file, strict=False)
#     countAllFacts = len(allFacts)
#     if limit < 0 or limit >= countAllFacts:
#         if random == False:
#             return allFacts
#         Rand.shuffle(allFacts)
#         return allFacts
#     if limit == 0:
#         return []
#     if random:
#         Rand.shuffle(allFacts)
#         requiredFacts = []
#         for i in range(limit):
#             requiredFacts.append(allFacts[i])
#         return requiredFacts
#     requiredFacts = []
#     for i in range(limit):
#         requiredFacts.append(allFacts[i])
#     return requiredFacts

# Uncharted 4
@app.get("/uncharted4/")
async def read_item(limit: int = -1, random: bool = False):
    with open('uncharted4.json', "r", encoding='utf-8') as json_file:
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
    return requiredFacts