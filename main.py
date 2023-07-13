from aiogram import executor
from create_bot import dp, bot
from keyboards import keyboard
from handlers import users

async def on_startup(_):
    print('Бот включен')

keyboards = keyboard.create_keyboards()
users.register_handlers_user(dp)

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)