# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Models import PokemonModel
from querys import new_pokemon, updatePokemon
from conecction import Neo4j_connexion, getlist
from add_infoNeo4J import loop_for_create
app = FastAPI()

# Listar desde pokeapi
# @app.get("/pokemons/")
# def list_public_pokemons():
#     data = getlist("https://pokeapi.co/api/v2/pokemon/?limit=200&offset=0")
#     if data:
#         createinfo = loop_for_create(data)
#         return createinfo
#     raise HTTPException(status_code=404, detail="No se pudo acceder a PokeAPI")

@app.get("/pokemons/")
def get_pokemons():
    list = """
    MATCH(p:Pokemon) RETURN p
    """
    result = Neo4j_connexion(list)
    if result:
        return result
    
# Crear Pokémon en Neo4j
@app.post("/pokemons/")
def create_pokemon(pokemon: PokemonModel):
    result = new_pokemon(pokemon)
    if result:
         return result


# # Actualizar Pokémon en Neo4j
@app.put("/pokemons/{id}")
def update_pokemon(id: str, pokemon: PokemonModel):
    result = updatePokemon(id, pokemon)
    if result:
        return result

# # Eliminar Pokémon
@app.delete("/pokemons/delete/{id}")
def delete_pokemon(id: str):
    query = "MATCH (p:Pokemon {id: $id}) SET p.active = False RETURN p"
    result = Neo4j_connexion(query, {"id": id})
    return result

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)