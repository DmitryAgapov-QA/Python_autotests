import requests

URL = 'https://api.pokemonbattle.me/v2/' 
TOKEN = 'TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '2216'


Body_create = {
    "name": "Пивчик",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
}

Body_change = {
    "pokemon_id": '27472',
    "name": "Бобр",
    "photo": "https://dolnikov.ru/pokemons/albums/017.png"
}

Body_to_catch = {
    "pokemon_id": '27472'
}
respons_create = requests.post(url=f'{URL}pokemons', headers=HEADER, json=Body_create)
print(respons_create.text)

pokemon_id = respons_create.json()['id']
print(pokemon_id)

respons_change = requests.put(url=f'{URL}pokemons', headers=HEADER, json=Body_change)
print(respons_change.text)

respons_to_catch = requests.post(url=f'{URL}trainers/add_pokeball', headers=HEADER, json=Body_to_catch)
print(respons_to_catch.text)


respons_list_pokemons = requests.get(url=f'{URL}trainers', params= {'sort': 'desc_price'})
print(respons_list_pokemons.text)

