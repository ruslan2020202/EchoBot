import asyncio
import logging

from aiogram import Bot, Dispatcher, types, filters, F
from config import token_api

bot = Bot(token_api)
dp = Dispatcher()
photo_id = None


@dp.message(filters.CommandStart())
async def cdm_start(message: types.Message):
    await message.answer('Привет')


@dp.message(filters.Command('help'))
async def cmd_help(message: types.Message):
    await message.answer('Это команда /help')


@dp.message(F.text == 'Как дела?')
async def how_are_you(message: types.Message):
    await message.reply('OK!')


@dp.message(F.photo)
async def photo(message: types.Message):
    global photo_id
    photo_id = message.photo[-1].file_id
    await message.reply(f'ID фото: {photo_id}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(dp.start_polling(bot))
    except KeyboardInterrupt:
        print('Exit')
