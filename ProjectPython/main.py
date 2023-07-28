import requests

token = 'dd50cd6e46a94c8688d95a7e5dfc7f35'
host = 'https://api.pokemonbattle.me:9104'                                           # Прод

'''response_create = requests.post(f'{host}/pokemons', json = {                      # Создание покемона
    "name": "generate",
    "photo": "generate"
}, headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})

print(response_create.text)'''



'''response_rename = requests.put(f'{host}/pokemons', json = {                          # Смена имени покемона
    "pokemon_id": "5584",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})

print(response_rename.text)'''



'''response_add = requests.post(f'{host}/trainers/add_pokeball', json = {               # Поймать в покебол
    "pokemon_id": "5584"
}, headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})

print(response_add.text)'''



response_trainers = requests.get(f'{host}/trainers?trainer_id=1860')                    # Информация по тренеру

print(response_trainers.text)