from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

btn1 = KeyboardButton(text=LEXICON_RU['animals_menu'])
btn2 = KeyboardButton(text=LEXICON_RU['anime'])
btn3 = KeyboardButton(text=LEXICON_RU['weather'])
btn4 = KeyboardButton(text=LEXICON_RU['game'])

menu_kb_builder = ReplyKeyboardBuilder()

menu_kb_builder.row(btn1, btn2, btn3, btn4,  width=2)

menu_kb: ReplyKeyboardMarkup = menu_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True)


button_dog = KeyboardButton(text=LEXICON_RU['dog'])
button_cat = KeyboardButton(text=LEXICON_RU['cat'])
button_fox = KeyboardButton(text=LEXICON_RU['fox'])
button_end =KeyboardButton(text=LEXICON_RU['end'])

animals_kb_builder = ReplyKeyboardBuilder()

animals_kb_builder.row(button_dog, button_cat, button_fox, button_end, width=1)

animals_kb: ReplyKeyboardMarkup = animals_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True)


button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True)


button_r = KeyboardButton(text=LEXICON_RU['rock'])
button_s = KeyboardButton(text=LEXICON_RU['scissors'])
button_p = KeyboardButton(text=LEXICON_RU['paper'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_r],
              [button_s],
              [button_p]],
    resize_keyboard=True)