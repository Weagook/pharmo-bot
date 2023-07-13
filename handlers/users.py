from aiogram import types, Dispatcher
from aiogram.types.input_file import InputFile
from aiogram.dispatcher import FSMContext
from create_bot import dp, bot, keyboards
from config import message_pres, SOURCE_DIR, LIST_PRES
from utils import sheets
from states import models
import os

async def launch(message: types.Message):
    try:
        await state.finish()
    except NameError:
        pass
    await message.answer('Для взаимодействия с нашим умным\nботом нажмите на интересующий Вас\nпункт меню ниже', reply_markup=keyboards['main_keyboard'])

async def message_controller(message: types.Message):
    if message.text == 'Задать вопрос эксперту':
        await models.KnowledgeBase.ENTRY_STATE.set()
        await message.answer('Задайте свой вопрос, я вас внимательно слушаю', reply_markup=keyboards['callback_entry_kb'])
    elif message.text == 'Материалы':
        await message.answer('Выберите категорию', reply_markup=keyboards['material_kb'])
    elif message.text == 'PO Talks':
        await message.answer('Ведущие инфекционисты, педиатры и отоларингологи:\nёмко и по делу о мифах, клинической базе\nи опыте применения Полиоксидония', reply_markup=keyboards['talks_kb'])
        

async def callback_controller(callback: types.CallbackQuery):
    if callback.data == 'research':
        await bot.send_message(chat_id=callback.message.chat.id, text='Реализовать блок "Исследования"')
    elif callback.data == 'present':
        await bot.send_message(chat_id=callback.message.chat.id, text=message_pres, reply_markup=keyboards['present_kb'])
    elif callback.data.startswith('presentation_'):
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=InputFile(os.path.join(SOURCE_DIR, LIST_PRES[int(callback.data[-1])-1]))
        )

async def getting_question(message: types.Message, state: FSMContext):
    print('Работает функция getting_question')
    result = sheets.database_search(message.text)
    if result:
        await message.answer(result)
    else:
        await message.answer('Результат в базе не найден. Связать вас с специалистом?')
    await models.KnowledgeBase.GET_RESPONSE.set()

async def choice_of_actions(message: types.Message, state: FSMContext):
    print('Работает функция choice_of_actions')
    if message.text == 'Назад':
        await state.finish()
        await message.answer('Выберите действие из меню', reply_markup=keyboards['main_keyboard'])
    elif message.text == 'Связаться с специалистом':
        await message.answer('В ближайшее время специалист свяжется с вами. Не перезагружайте бота!')
    
    

def register_handlers_user(dp: Dispatcher) -> None:
    dp.register_message_handler(launch, commands=['start'], state='*')
    dp.register_message_handler(getting_question, state=models.KnowledgeBase.ENTRY_STATE)
    dp.register_message_handler(choice_of_actions, state=models.KnowledgeBase.GET_RESPONSE)
    dp.register_message_handler(message_controller)
    dp.register_callback_query_handler(callback_controller)