
from Models import PokemonModel
from conecction import Neo4j_connexion


def new_pokemon(pokemon: PokemonModel):
    query = """
    CREATE (p:Pokemon {
            id: $id,
            active: $active,
            name: $name,
            height: $height,
            weight: $weight,
            types: $types
        }
    )
    RETURN p
    """
    result = Neo4j_connexion(query, pokemon.dict())
    
def updatePokemon(id: str, pokemon: PokemonModel):
    query = "MATCH (p:Pokemon {id: $id}) "
    set_clauses = []
    params = {"id": id}
    if pokemon.name is not None:
        set_clauses.append("p.name = $name")
        params["name"] = pokemon.name
    if pokemon.active is not None:
        set_clauses.append("p.active = $active")
        params["active"] = pokemon.active
    if pokemon.height is not None:
        set_clauses.append("p.height = $height")
        params["height"] = pokemon.height
    if pokemon.weight is not None:
        set_clauses.append("p.weight = $weight")
        params["weight"] = pokemon.weight
    if pokemon.types is not None:
        set_clauses.append("p.types = $types")
        params["types"] = pokemon.types

    if not set_clauses:
        raise ValueError("No hay campos para actualizar")

    query += "SET " + ", ".join(set_clauses)
    query += " RETURN p"

    result = Neo4j_connexion(query, params)
    return result
