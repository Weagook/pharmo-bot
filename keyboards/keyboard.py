from aiogram import types
from config import LIST_FILES
import os

def create_kb(list_files: list, key: str) -> types.InlineKeyboardMarkup:
    '''
    Создает клавиатуру по списку презентаций.
    Возвращает клавиатуру класса InlineKeyboardMarkup
    '''
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = list()
    i = 1
    for file in list_files:
        button = types.InlineKeyboardButton(i, callback_data=f'{key}_{i}')
        buttons.append(button)
        i += 1
    keyboard.add(*buttons)

    return keyboard

def create_keyboards() -> dict:
    '''
    Функция создает все клавиатуры которые используются в боте
    Возвращает словарь с клавиатурами
    '''
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
    instruction_kb = create_kb(LIST_FILES['instructions'], 'instructions')

    # Создание клавиатуры с презентациями
    present_kb = create_kb(LIST_FILES['materials'], 'materials')

    # Клавиатура для лора
    lore_kb = create_kb(LIST_FILES['lore'], 'lore')

    # Клавиатура для педиатра
    pediatrics_kb = create_kb(LIST_FILES['pediatrics'], 'pediatrics')

    # Клавиатура для терапевта
    therapy_kb = create_kb(LIST_FILES['therapy'], 'therapy')

    # Клавиатура для PO Talks
    talks_kb = types.InlineKeyboardMarkup(row_width=1)
    b_youtube = types.InlineKeyboardButton('Смотреть на YouTube', url='https://www.youtube.com/watch?v=IMs2W8IlfvM')
    talks_kb.add(b_youtube)

    # Клавиатура выхода из состояний в блоке "Обратная связь"
    back_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cb_back = types.KeyboardButton('Назад')
    back_kb.add(cb_back)

    keyboards = dict()

    keyboards['main_keyboard'] = main_keyboard
    keyboards['material_kb'] = material_kb
    keyboards['present_kb'] = present_kb
    keyboards['talks_kb'] = talks_kb
    keyboards['back_kb'] = back_kb
    keyboards['research_kb'] = research_kb
    keyboards['lore_kb'] = lore_kb
    keyboards['pediatrics_kb'] = pediatrics_kb
    keyboards['therapy_kb'] = therapy_kb
    keyboards['instruction_kb'] = instruction_kb

    return keyboards
