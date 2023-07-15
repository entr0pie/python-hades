#!/bin/python3

from dotenv import dotenv_values
from neomodel import config

def setupDatabase() -> bool:
    """
    Configure the neomodel connection though .env
    """
    
    env = dotenv_values(".env")
    user: str = env.get('NEO4J_USERNAME')
    password: str = env.get('NEO4J_PASSWORD')
    address: str = env.get('NEO4J_ADDRESS')
    port: str = env.get('NEO4J_BOLT_PORT')
    assert (user and password and address and port)
    
    config.DATABASE_URL = f"bolt://{user}:{password}@{address}:{port}"
