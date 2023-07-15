from aiogram import types
from config import LIST_PRES, LIST_PRES_LORE, LIST_PRES_PEDIATRICS, LIST_PRES_THERAPY, LIST_PRES_INSTRUCTION
import os

def create_keyboards() -> dict:
    keyboards = dict()
    # Главная клавиатура
    main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b_question = types.KeyboardButton('Задать вопрос эксперту')
    b_materials = types.KeyboardButton('Материалы')
    b_talks = types.KeyboardButton('PO Talks')
    b_instr = types.KeyboardButton('Инструкции')
    b_callback = types.KeyboardButton('Обратный звонок', request_contact=True)
    main_keyboard.add(b_question).row(b_materials, b_talks).row(b_instr, b_callback)

    # Клавиатура раздела "Материалы"
    material_kb = types.InlineKeyboardMarkup(row_width=1)
    b_research = types.InlineKeyboardButton('Исследования', callback_data='research')
    b_present = types.InlineKeyboardButton('Презентация', callback_data='present')
    material_kb.add(b_research).add(b_present)

    # Клавиатура "Исследования"
    research_kb = types.InlineKeyboardMarkup(row_width=2)
    b_pediatrics = types.InlineKeyboardButton('Педиатрия', callback_data='pediatrics')
    b_therapy = types.InlineKeyboardButton('Терапия', callback_data='therapy')
    b_lore = types.InlineKeyboardButton('Лор', callback_data='lore')
    research_kb.row(b_pediatrics, b_lore).add(b_therapy)

    # Клавиатура "Инструкции"
    instruction_kb = types.InlineKeyboardMarkup(row_width=3)
    buttons_instr = list()
    counter = 1
    for pres in LIST_PRES_INSTRUCTION:
        button = types.InlineKeyboardButton(counter, callback_data=f'instruction_{counter}')
        buttons_instr.append(button)
        counter += 1
    instruction_kb.add(*buttons_instr)

    # Создание клавиатуры с презентациями
    present_kb = types.InlineKeyboardMarkup(row_width=3)
    buttons_pres = list()
    counter = 1
    for pres in LIST_PRES:
        button = types.InlineKeyboardButton(counter, callback_data=f'presentation_{counter}')
        buttons_pres.append(button)
        counter += 1
    present_kb.add(*buttons_pres)

    # Клавиатура для лора
    lore_kb = types.InlineKeyboardMarkup(row_width=3)
    buttons_lore = list()
    counter = 1
    for pres in LIST_PRES_LORE:
        button = types.InlineKeyboardButton(counter, callback_data=f'lore_{counter}')
        buttons_lore.append(button)
        counter += 1
    lore_kb.add(*buttons_lore)

    # Клавиатура для педиатра
    pediatrics_kb = types.InlineKeyboardMarkup(row_width=3)
    buttons_pediatrics = list()
    counter = 1
    for pres in LIST_PRES_PEDIATRICS:
        button = types.InlineKeyboardButton(counter, callback_data=f'pediatrics_{counter}')
        buttons_pediatrics.append(button)
        counter += 1
    pediatrics_kb.add(*buttons_pediatrics)

    # Клавиатура для терапевта
    therapy_kb = types.InlineKeyboardMarkup(row_width=3)
    buttons_therapy = list()
    counter = 1
    for pres in LIST_PRES_THERAPY:
        button = types.InlineKeyboardButton(counter, callback_data=f'therapy_{counter}')
        buttons_therapy.append(button)
        counter += 1
    therapy_kb.add(*buttons_therapy)

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
    keyboards['research_kb'] = research_kb
    keyboards['lore_kb'] = lore_kb
    keyboards['pediatrics_kb'] = pediatrics_kb
    keyboards['therapy_kb'] = therapy_kb
    keyboards['instruction_kb'] = instruction_kb

    return keyboards
