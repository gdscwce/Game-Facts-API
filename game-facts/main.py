from fastapi import FastAPI, File,Response, Header
from fastapi.responses import FileResponse, RedirectResponse
from typing import Optional
from deta import Deta
from pydantic import BaseModel
import hashlib
import jwt
import uuid
import json
from datetime import datetime, timedelta
from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from math import radians, cos, sin, asin, sqrt
import time

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