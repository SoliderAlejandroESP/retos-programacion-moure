import requests

"""
Ejercicio
"""

"""
r = requests.get('https://www.youtube.com/')

if r.status_code == 200:
  print(r.content)
else:
  print(f'Error: {r.status_code}')
"""


"""
Extra
"""

# https://pokeapi.co/api/v2/pokemon/{name or id}

pokemon = input('Inserte el nombre o el id de un pokemon: ')

poke_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')

if poke_response.status_code == 200:
  data = poke_response.json()
  print('Nombre:', data['name'])
  print('Id:', data['id'])
  print('Peso:', data['weight'])
  print('Altura:', data['height'])
  
  types = data['types']
  print('Tipo(s): ')
  for type in types:
    print(type['type']['name'])
  
  games = data['game_indices']
  print('Juego(s): ')
  for game in games:
    print(game['version']['name'])

  poke_response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}')

  if poke_response.status_code == 200:
    data = poke_response.json()
    evolution_chain_url = data['evolution_chain']['url']
    poke_response = requests.get(evolution_chain_url)

    if poke_response.status_code == 200:
      data = poke_response.json()

      print("Cadena de evolución:")

      def get_evolves(data):
        print(data["species"]["name"])
        if "evolves_to" in data:
          for evolve in data["evolves_to"]:
            get_evolves(evolve)

      get_evolves(data["chain"])
      
      
    else:
      print(f'Error {poke_response.status_code} al obtener la cadena de evolución del pokemon')
  else:
    print(f'Error {poke_response.status_code} al obtener la especie del pokemon')
else:
  print(f'Error {poke_response.status_code} al obtener el pokemon')