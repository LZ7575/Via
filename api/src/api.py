from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI
from redis import Redis
from src import db

app = FastAPI()

# Required cors change for localhost and dev testing
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
def get_redis():
  return Redis(connection_pool=db.pool)

# Any undefined page
@app.get("/")
async def root() -> dict:
    return {"message": "Not Found"}

# Database value addition
@app.post("/add")
async def add_data(value: db.Bitcoin, database: Redis = Depends(get_redis)) -> None:
    database.set(value.timestamp, value.price)
    
# Get data from database
@app.get("/get")
async def get_data(database: Redis = Depends(get_redis)) -> dict:
    keys = database.keys()
    return keys.__dict__