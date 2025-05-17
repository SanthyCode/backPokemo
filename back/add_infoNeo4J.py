import requests
from Models import PokemonModel
from conecction import Neo4j_connexion


def loop_for_create(info):
    for i in info["results"]:
        data = requests.get(i["url"])
        if data.status_code == 200:
            info = data.json()
            model_data = {
                "id": str(info["id"]),
                "active": True,
                "name": info["name"],
                "height": info["height"],
                "weight": info["weight"],
                "types": [t["type"]["name"] for t in info["types"]],
                "sprites": info["sprites"]["other"]["dream_world"]["front_default"]
            }
            pokemon = PokemonModel(**model_data)  # ✅ Crea una instancia del modelo
            new_list = add_info(pokemon)          # ✅ Pasa el modelo, no un dict
    return new_list

        
   
def add_info(pokemon: PokemonModel):
    query = """
    MATCH (r:Root_Pokemons)
    CREATE (b:Pokemon {
        id: $id,
        active: true,
        name: $name,
        height: $height,
        weight: $weight,
        types: $types,
        sprites: $sprites
    })
    MERGE (r)-[:THIS_POKEMON]->(b)
    RETURN b
    """
    params = {
        "id": pokemon.id,
        "active": True,
        "name": pokemon.name,
        "height": pokemon.height,
        "weight": pokemon.weight,
        "types": pokemon.types,
        "sprites": pokemon.sprites
    }
    result = Neo4j_connexion(query, params)
    return result