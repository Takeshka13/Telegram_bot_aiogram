import random
import requests

from lexicon.lexicon_ru import LEXICON_RU

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_FOX_URL = 'https://randomfox.ca/floof/'
API_DOG_URL = 'https://dog.ceo/api/breeds/image/random'
ERROR_CAT = 'https://i.imgur.com/Wl7vgem.png'
ERROR_FOX = 'https://i.imgur.com/8yvMlsw.png'

def get_random_cat():
    cat_response: requests.Response
    cat_link: str

    cat_response = requests.get(API_CATS_URL)
    if cat_response.status_code == 200:
        cat_link = cat_response.json()[0]['url']
        return cat_link
    else:
        bad_cat_response = requests.get(ERROR_CAT)
        bad_cat_link = bad_cat_response.json()[0]['scr']
        return bad_cat_link

def get_random_fox():
    fox_response: requests.Response
    fox_link: str

    fox_response = requests.get(API_FOX_URL)
    if fox_response.status_code == 200:
        fox_link = fox_response.json()['image']
        return fox_link
    else:
        bad_fox_response = requests.get(ERROR_FOX)
        bad_fox_link = bad_fox_response.json()[0]['scr']
        return bad_fox_link

def get_random_dog():
    dog_response: requests.Response
    dog_link: str

    dog_response = requests.get(API_DOG_URL)
    if dog_response.status_code == 200:
        dog_link = dog_response.json()['message']
        return dog_link
    else:
        bad_fox_response = requests.get(ERROR_FOX)
        bad_fox_link = bad_fox_response.json()[0]['scr']
        return bad_fox_link

def get_random_anime():
    anime_response: requests.Response
    anime_link: str

    list = ('kiss', 'love', 'evillaugh', 'cry')
    filt = random.choice(list)

    anime_response = requests.get(f'https://api.otakugifs.xyz/gif?reaction={filt}&format=gif')
    if anime_response.status_code == 200:
        anime_link = anime_response.json()['url']
        return anime_link
    else:
        bad_anime_response = requests.get(ERROR_FOX)
        bad_anime_link = bad_anime_response.json()[0]['scr']
        return bad_anime_link


def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])

def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key

def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'