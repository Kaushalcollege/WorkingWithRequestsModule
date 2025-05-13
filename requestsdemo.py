import requests as r
# for this, we have to install requests module.
'''
using pip install requests, in the terminal.
'''
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}" # string formatting.
    response = r.get(url)
    if response.status_code == 200:
        pokemon_data = response.json() # convert the json to a dictionary
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon = input("Enter a pokemon name: ")
pokemon.lower()
print(pokemon.lower())
pokemon_info = get_pokemon_info(pokemon)

if pokemon_info:
    print(f"Pokemon name: {pokemon_info["name"].title()}")
    print(f"Pokemon name: {pokemon_info["id"]}")
    print(f"Pokemon name: {pokemon_info["weight"]}")
    print(f"Pokemon name: {pokemon_info["height"]}")
    print(f"Pokemon name: {pokemon_info["abilities"]}")