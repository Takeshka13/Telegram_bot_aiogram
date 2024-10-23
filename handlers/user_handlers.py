from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from keyboards.keyboards import menu_kb, animals_kb, game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner, get_random_cat, get_random_fox, get_random_anime, get_random_dog

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

@router.message(Command(commands='menu'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/menu'], reply_markup=menu_kb)

@router.message(F.text == LEXICON_RU['animals_menu'])
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['animals'], reply_markup=animals_kb)

@router.message(F.text == LEXICON_RU['dog'])
async def process_no_answer(message: Message):
    await message.answer_photo(get_random_dog())

@router.message(F.text == LEXICON_RU['cat'])
async def process_no_answer(message: Message):
    await message.answer_photo(get_random_cat())

@router.message(F.text == LEXICON_RU['fox'])
async def process_no_answer(message: Message):
    await message.answer_photo(get_random_fox())

@router.message(F.text == LEXICON_RU['end'])
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['cancel_animals'], reply_markup=menu_kb)

@router.message(F.text == LEXICON_RU['weather'])
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['city'])

@router.message(F.text == LEXICON_RU['anime'])
async def process_no_answer(message: Message):
    await message.answer_animation(get_random_anime())

@router.message(F.text == LEXICON_RU['game'])
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/game'], reply_markup=yes_no_kb)

@router.message(Command(commands='gamehelp'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/gamehelp'], reply_markup=yes_no_kb)

@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)

@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'], reply_markup=menu_kb)

@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)





