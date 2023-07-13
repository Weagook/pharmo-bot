from aiogram import types
from config import LIST_PRES
import os

def create_keyboards() -> dict:
    keyboards = dict()
    # Главная клавиатура
    main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b_question = types.KeyboardButton('Задать вопрос эксперту')
    b_materials = types.KeyboardButton('Материалы')
    b_talks = types.KeyboardButton('PO Talks')
    b_instr = types.KeyboardButton('Инструкции')
    b_callback = types.KeyboardButton('Обратный звонок')
    main_keyboard.add(b_question).row(b_materials, b_talks).row(b_instr, b_callback)

    # Клавиатура раздела "Материалы"
    material_kb = types.InlineKeyboardMarkup(row_width=1)
    b_research = types.InlineKeyboardButton('Исследования', callback_data='research')
    b_present = types.InlineKeyboardButton('Презентация', callback_data='present')
    material_kb.add(b_research).add(b_present)

    # Создание клавиатуры с презентациями
    present_kb = types.InlineKeyboardMarkup(row_width=3)
    buttons_pres = list()
    counter = 1
    for pres in LIST_PRES:
        button = types.InlineKeyboardButton(counter, callback_data=f'presentation_{counter}')
        buttons_pres.append(button)
        counter += 1
    present_kb.add(*buttons_pres)

    # Клавиатура для PO Talks
    talks_kb = types.InlineKeyboardMarkup(row_width=1)
    b_youtube = types.InlineKeyboardButton('Смотреть на YouTube', url='https://www.youtube.com/watch?v=IMs2W8IlfvM')
    talks_kb.add(b_youtube)

    # Клавиатура для обратной связи
    callback_entry_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    callback_getans_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cb_back = types.KeyboardButton('Назад')
    cb_call = types.KeyboardButton('Связаться с специалистом')
    callback_entry_kb.add(cb_back).add(cb_call)
    callback_getans_kb.add(cb_back)

    keyboards['main_keyboard'] = main_keyboard
    keyboards['material_kb'] = material_kb
    keyboards['present_kb'] = present_kb
    keyboards['talks_kb'] = talks_kb
    keyboards['callback_entry_kb'] = callback_entry_kb
    keyboards['callback_getans_kb'] = callback_getans_kb

    return keyboards
