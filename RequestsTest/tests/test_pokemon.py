import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2/' 
TOKEN = 'TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '2216'

def test_status_code():
    respons = requests.get(url=f'{URL}trainers', headers=HEADER, params={'level':'1'})
    assert respons.status_code == 200
    
def test_body_respons():
    respons_get = requests.get(url=f'{URL}trainers', headers=HEADER, params={'trainer_id': TRAINER_ID})
    assert respons_get.json()['data'][0]['id'] == TRAINER_ID  


