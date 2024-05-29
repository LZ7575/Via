from fastapi.logger import logger
from redis import ConnectionPool
from pydantic import BaseModel
from os import getenv

# Definition of a pet with it's values
class Bitcoin(BaseModel):
    timestamp: str
    price: float

# Connecting and returning a database instance
def create_redis():
    logger.warning("Connected to database")
    return ConnectionPool(
        host=getenv('REDIS_HOST'), 
        port=getenv('REDIS_PORT'), 
        db=0, 
        decode_responses=True
    )

pool: ConnectionPool = create_redis()