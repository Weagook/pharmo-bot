from aiogram import types, Dispatcher
from aiogram.types.input_file import InputFile
from aiogram.dispatcher import FSMContext
from create_bot import dp, bot, keyboards
from utils import sheets
from states import models 
import os
from config import (
    SOURCE_DIR, LIST_PRES, MANAGER_ID,
    LIST_PRES_LORE, LIST_PRES_PEDIATRICS, LIST_PRES_THERAPY,
    LIST_PRES_INSTRUCTION, message_pres_lore, message_pres_pediatrics,
    message_pres_therapy, message_source_pres, message_pres_instr
)


async def launch(message: types.Message):
    try:
        await state.finish()
    except NameError:
        pass
    await message.answer('Для взаимодействия с нашим умным\nботом нажмите на интересующий Вас\nпункт меню ниже', reply_markup=keyboards['main_keyboard'])

async def message_controller(message: types.Message):
    if message.text == 'Задать вопрос эксперту':
        await models.KnowledgeBase.ENTRY_STATE.set()
        await message.answer('Задайте свой вопрос, я вас внимательно слушаю', reply_markup=keyboards['callback_getans_kb'])
    elif message.text == 'Материалы':
        await message.answer('Выберите категорию', reply_markup=keyboards['material_kb'])
    elif message.text == 'PO Talks':
        await message.answer('Ведущие инфекционисты, педиатры и отоларингологи:\nёмко и по делу о мифах, клинической базе\nи опыте применения Полиоксидония', reply_markup=keyboards['talks_kb'])
    elif message.text == 'Инструкции':
        await message.answer(message_pres_instr, reply_markup=keyboards['instruction_kb'])
        

async def callback_controller(callback: types.CallbackQuery):
    if callback.data == 'research':
        await bot.send_message(chat_id=callback.message.chat.id, text='Выберите раздел', reply_markup=keyboards['research_kb'])
    elif callback.data == 'present':
        await bot.send_message(chat_id=callback.message.chat.id, text=message_source_pres, reply_markup=keyboards['present_kb'])
    elif callback.data == 'lore':
        await bot.send_message(chat_id=callback.message.chat.id, text=message_pres_lore, reply_markup=keyboards['lore_kb'])
    elif callback.data == 'pediatrics':
        await bot.send_message(chat_id=callback.message.chat.id, text=message_pres_pediatrics, reply_markup=keyboards['pediatrics_kb'])
    elif callback.data == 'therapy':
        await bot.send_message(chat_id=callback.message.chat.id, text=message_pres_therapy, reply_markup=keyboards['therapy_kb'])
    elif callback.data.startswith('presentation_'):
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=InputFile(os.path.join(os.path.join(SOURCE_DIR, 'materials'), LIST_PRES[int(callback.data[-1])-1]))
        )
    elif callback.data.startswith('therapy_'):
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=InputFile(os.path.join(os.path.join(SOURCE_DIR, 'therapy'), LIST_PRES_THERAPY[int(callback.data[-1])-1]))
        )
    elif callback.data.startswith('pediatrics_'):
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=InputFile(os.path.join(os.path.join(SOURCE_DIR, 'pediatrics'), LIST_PRES_PEDIATRICS[int(callback.data[-1])-1]))
        )
    elif callback.data.startswith('lore_'):
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=InputFile(os.path.join(os.path.join(SOURCE_DIR, 'lore'), LIST_PRES_LORE[int(callback.data[-1])-1]))
        )
    elif callback.data.startswith('instruction_'):
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=InputFile(os.path.join(os.path.join(SOURCE_DIR, 'instructions'), LIST_PRES_INSTRUCTION[int(callback.data[-1])-1]))
        )

async def getting_question(message: types.Message, state: FSMContext):
    if message.text == 'Назад':
        await message.answer('Выберите функцию в меню', reply_markup=keyboards['main_keyboard'])
    else:
        result = await sheets.read_google_sheet(checked_object=message.text, revise=True)
        if result:
            await message.answer(result, reply_markup=keyboards['main_keyboard'])
        else:
            await message.answer('Результат в базе не найден. Специалист свяжется с вами в ближайшее время и ответит на ваш вопрос.', reply_markup=keyboards['main_keyboard'])
            await bot.send_message(chat_id=MANAGER_ID, text=f'[Клиент {message.from_user.id}]: {message.text}')
    await state.finish()
    
async def giveAccesSheet(message: types.Message):
    if message.from_user.id == MANAGER_ID:
        try:
            await state.finish()
        except NameError:
            pass
        await message.answer('Пожалуйста, напишите google почту пользователя, которому нужно выдать доступ. Пример: test_company@gmail.com')
        await models.GiveAccessSheet.ENTRY_STATE.set()

async def collection_email_access(message: types.Message):
    email = message.text.lower().replace(' ', '')
    if email.endswith('@gmail.com'):
        await sheets.give_access_sheet(email)
        await message.answer('Доступ выдан!')
        try:
            await state.finish()
        except NameError:
            pass
    else:
        await message.answer('Неккоретный email. Попробуйте еще раз.')

async def manager_answer(message: types.Message):
    if message.from_user.id == MANAGER_ID:
        argv = message.text.split(' ')
        id_user = argv[1]
        message_answer = '[Специалист]: ' + ' '.join(argv[2:])
        await bot.send_message(chat_id=id_user, text=message_answer)

async def collection_contact(message: types.Message):
    contact = message.contact
    message_from = f'Запрос на обратную связь: {contact.first_name} - {contact.phone_number}'
    await bot.send_message(chat_id=MANAGER_ID, text=message_from)


def register_handlers_user(dp: Dispatcher) -> None:
    dp.register_message_handler(launch, commands=['start'], state='*')
    dp.register_message_handler(giveAccesSheet, commands=['access'], state='*')
    dp.register_message_handler(manager_answer, commands=['answer'], state='*')
    dp.register_message_handler(collection_contact, content_types=types.ContentType.CONTACT, state='*')
    dp.register_message_handler(collection_email_access, state=models.GiveAccessSheet.ENTRY_STATE)
    dp.register_message_handler(getting_question, state=models.KnowledgeBase.ENTRY_STATE)
    dp.register_message_handler(message_controller)
    dp.register_callback_query_handler(callback_controller)