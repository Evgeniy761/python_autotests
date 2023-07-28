import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = 'dd50cd6e46a94c8688d95a7e5dfc7f35'



def test_status_code():
    response_trainers = requests.get(f'{host}/trainers', params= {'trainer_id' : 1860})                # Проверяем статус 200
    assert response_trainers.status_code == 200

def test_part_of_body():
    response_trainers = requests.get(f'{host}/trainers', params= {'trainer_id' : 1860})                # Ищем в теле ответа конкретную строчку
    assert response_trainers.json()['trainer_name'] == 'Валера'