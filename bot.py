import asyncio
import logging

from aiogram import Bot, Dispatcher, types, filters, F

from config import token_api

bot = Bot(token_api)
dp = Dispatcher()


@dp.message(filters.CommandStart())
async def cdm_start(message: types.Message):
    await message.answer('Привет, я ЭхоБот')


@dp.message(F.text)
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(dp.start_polling(bot))
    except KeyboardInterrupt:
        print('Exit')
