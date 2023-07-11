from aiogram import types, executor, Dispatcher, Bot
from aiogram.types.input_file import InputFile
from keyboard import *

# Получение токена из виртуального окружения
# TOKEN = os.environ.get('TOKEN_TELEGRAM')
TOKEN = '6145310970:AAFV4_w-r9jKO1pkf4EpXonGqABrfEUWgrM'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def launch(message: types.Message):
    await message.answer(start_message, reply_markup=main_keyboard)

@dp.message_handler()
async def message_controller(message: types.Message):
    if message.text == 'Задать вопрос эксперту':
        await message.answer('Необходимо реализовать блок "Консультация"')
    elif message.text == 'Материалы':
        await message.answer('Выберите категорию', reply_markup=material_kb)
    elif message.text == 'PO Talks':
        await message.answer(talks_message, reply_markup=talks_kb)

@dp.callback_query_handler()
async def callback_controller(callback: types.CallbackQuery):
    if callback.data == 'research':
        await message.answer('Реализовать блок "Исследования"')
    elif callback.data == 'present':
        await bot.send_message(chat_id=callback.message.chat.id, text=message_pres, reply_markup=present_kb)
    elif callback.data.startswith('presentation_'):
        # Отправляем документ. Нужно выбрать более подходящий вариант
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=InputFile(os.path.join(PRESENT_DIR, presentations[int(callback.data[-1])-1]))
        )

        # file_path = os.path.join(PRESENT_DIR, presentations[int(callback.data[-1])-1])
        # with open(file_path, 'rb') as file:
        #     await bot.send_document(
        #         chat_id=callback.message.chat.id,
        #         document=file
        #     )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)