import time
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "6012629869:AAH_Ije1csNDeGhHRuj0iLs6Zwwg1AoJImM"
MSG = "Совершал ли ты намаз сегодня, {}?"
MSG1 = 'Выпьешь пива, будешь ссать криво!'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
	user_id = message.from_user.id
	user_name = message.from_user.first_name
	user_full_name = message.from_user.full_name
	logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
	await message.reply(f"Привет, {user_full_name}! Будешь пива?")
 
	for i in range(5):
			time.sleep(1)
			await bot.send_message(user_id, MSG.format(user_name))
			await bot.send_message(user_id, MSG.format(user_name))


if __name__ == '__main__':
	executor.start_polling(dp)
