# conecction.py
from neo4j import GraphDatabase
import requests

URI = "neo4j+s://e9f925f1.databases.neo4j.io"
USER = "neo4j"
PASSWORD = "uWnRvAf2Mc7rlytM72e8jk3Mr16kUvUsSk6jYIPr59g"

info_api = "https://pokeapi.co/api/v2/pokedex/"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def Neo4j_connexion(query: str, parameters: dict = None):
    with driver.session() as session:
        result = session.run(query, parameters or {})
        return [record.data() for record in result]

def get_pokemon_list(limit=200, offset=0):
    url = f"{info_api}"
    res = requests.get(url)
    return res.json() if res.status_code == 200 else None

def get_pokemon_data(name: str):
    url = f"{info_api}{name.lower()}"
    res = requests.get(url)
    return res.json() if res.status_code == 200 else None

def getlist(info):
    data = requests.get(info)
    if data.status_code == 200:
        return data.json()
    
