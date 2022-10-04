from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import filehandler
from random import choices
app = FastAPI(
    title="Game facts API",
    description="Fetch interesting facts about popular games",
    version="1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "The API is operational"}


@app.get("/fact/game={game}")
async def fact(game: str or None = None, limit: int = 1):
    # games can be seperated by &
    game_list = [x.strip() for x in game.split('&')]
    response = []
    tempresponse = []
    factcount = 0
    try:
        for games in game_list:
            handler = filehandler.open_file(games)
            fact, count = handler[0], handler[1]
            tempresponse.append(fact)
            factcount+=count
        if limit == -1 or factcount<limit:
            response.extend(tempresponse)
        else:
            for index,games in enumerate(game_list):
                response.append(choices(tempresponse[index],k=limit))
    except Exception as e:
        raise HTTPException(500, e)
    

    return response
